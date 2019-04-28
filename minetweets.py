#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:52:44 2019

@author: cbailey
"""

import simplejson as json
import re

rawText = []


def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

with open('tweets.json', 'r') as file:
    jsonfile= json.loads(file.read())
    for tweet in jsonfile:
        print("TWEET")
        print(tweet)
        print("TWEET TEXT")
        print(tweet['text'])
        print("CLEANED")
        print(clean_tweet(tweet['text']))
        rawText.append(clean_tweet(tweet['text']))
        
        

    