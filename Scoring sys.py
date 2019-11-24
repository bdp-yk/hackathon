# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:15:03 2019

@author: Riadh
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
analyser = SentimentIntensityAnalyzer()
import json

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    """print("{:-<40} {}".format(sentence, str(score)))"""
    return score

def calc(listName):
    S=0
    for k in listName:
        S= S+sentiment_analyzer_scores(k)['pos']+(sentiment_analyzer_scores(k)['neu']/2)  
    return(S/len(listName)*100)
        
    
with open('C:/Users/Riadh/Desktop/data.json',encoding="utf8") as f:
  data = json.load(f)
  
print(calc(data['Rio de Janeiro']['comments']))





    





























