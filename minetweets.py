#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:52:44 2019

@author: cbailey
"""

import simplejson as json
import re
from textblob import TextBlob

mytweets = []


def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

with open('tweets.json', 'r') as file:
    jsonfile= json.loads(file.read())
    for tweet in jsonfile:
        print(type(tweet))
        
        print("TWEET")
        print(tweet)
        print("TWEET TEXT")
        print(tweet['full_text'])
        print("CLEANED")
        clean = clean_tweet(tweet['full_text'])
        tweet["clean_text"] = clean
        blob = TextBlob(clean)
        print("SENTIMENT")
        print(blob.sentiment)
        tweet["sentiment"] = blob.sentiment
        mytweets.append(tweet)
        
with open('processed_tweets.json', 'w', encoding='utf8') as file:
    json.dump(mytweets, file, ...)
        
        
        

    