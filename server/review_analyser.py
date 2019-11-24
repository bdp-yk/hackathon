# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:15:03 2019

@author: Riadh
"""

import json

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

with open('./data.json',encoding="utf8") as f:
  data = json.load(f)

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    """print("{:-<40} {}".format(sentence, str(score)))"""
    return score

def calc(listName):
    S=0
    for k in listName:
        S= S+sentiment_analyzer_scores(k)['pos']+(sentiment_analyzer_scores(k)['neu']/2)  
    return(S/len(listName)*100)


def job(place):
    return calc(data[place]['comments'])  
    