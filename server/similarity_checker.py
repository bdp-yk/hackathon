# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:15:47 2019

@author: go home
"""
import json
from flask import jsonify
import random
import cv2
import numpy as np
import scipy
from scipy.misc import imread
import _pickle as cPickle
import os
import matplotlib.pyplot as plt
from flask import jsonify

def extract_features(image_path, vector_size=32):
    image = imread(image_path, mode="RGB")
    try:
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None

    return dsc

#extract_features(r'c:\\Users\\go home\\Pictures\\MonCV\\overview\\images\\img2.jpg', vector_size=32)

images_path=r'C:\\Users\\fedi\\Desktop\\Nouveau dossier'



def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        cPickle.dump(result, fp)
        print(fp)

#batch_extractor(images_path, pickled_db_path="features.pck")


class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path,'rb') as fp:
            self.data = cPickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

#m= Matcher('features.pck')


def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    
x=[]
dic_f=[]
dic={}
pos = 0
def run(sample):
    images_path = r'C:\\Users\\fedi\\Desktop\\img places'
   # files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # getting 3 random images 
#    sample = files[1]
    batch_extractor(images_path)

    ma = Matcher('features.pck')
    with open('C:\\Users\\fedi\\Desktop\\Hackathon\\server\\data.json',encoding="utf8") as f:
        data = json.load(f)

    print('Query image ==========================================')
    #show_img(sample)
    names, match = ma.match(sample, topn=3)
    print('Result images ========================================')
    for i in range(3):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
        print('Match %s' % (1-match[i]))
        x.append(os.path.join(images_path, names[i]))
        print(x[i][names[i].rfind('\\')+1:])
        dic.update({i:x[i][names[i].rfind('\\')+1:names[i].rfind('.')]})
        dic_f.append({x[i][names[i].rfind('\\')+1:names[i].rfind('.')]:data[dic[i]]})

    """ return jsonify(dic_f) """
    
    
    
if __name__ == "__main__":
    run("C:\\Users\\fedi\\Desktop\\img places\\rabat.jpg")

