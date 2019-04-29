#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:01:51 2019

@author: cbailey
"""

import tweepy
import simplejson as json


def yo(oldest,new_tweets,alltweets):
    while len(new_tweets) > 0:  
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = '@realDonaldTrump',count=200,max_id=oldest, tweet_mode='extended')
        
        # save most recent tweets
        alltweets.extend(new_tweets)
        
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print("...%s tweets downloaded so far" % (len(alltweets)))
    with open('tweets.json', 'w', encoding='utf8') as file:
        json.dump([tweet._json for tweet in alltweets], file, ...)
        

# Consumer keys and access tokens, used for OAuth
consumer_key = 'hlEUwtFtEklK0AVP0lZpC4kyE'
consumer_secret = 'NPEkJ0gMxY9AeQbOdhNHxrsUOPiESUTn6bJR9sgHWVyX4aZkET'
access_token = '1121186735843631105-txuyXIsngFGfFyjbOjFK5H4MpMCyrK'
access_token_secret = 'ajFOXhYXMckBD3DfATTWSiZ5ZWq4vpo8RojffzmNEc24G'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', tweet_mode="extended").items():
#    print(status.full_text)
    

alltweets = []  

# make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = '@realDonaldTrump',count=200, tweet_mode='extended')

# save most recent tweets
alltweets.extend(new_tweets)

oldest = alltweets[-1].id

yo(oldest,new_tweets,alltweets)



