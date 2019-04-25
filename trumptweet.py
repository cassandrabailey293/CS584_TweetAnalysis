#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:01:51 2019

@author: cbailey
"""

import tweepy

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

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', tweet_mode="extended").items():
    print(status.full_text)