# -*- coding: utf-8 -*-

import tweepy
import pandas as pd
from textblob import TextBlob
import csv

import sys
print (sys.path)

import os
os.getcwd()

consumer_key = 'ts8RhO1B1qIzdSLaDsaise89a'
consumer_secret = 'A4ZawHMrKiAaoxfQhmjrW5F2gWwgjh9jhCuvczy8cymLaTJfES'

access_token = '929606650415136768-Ok0ca8lkQk7oD8xNUqKWKg9VyoEXJRV'
access_token_secret = '5mJm07yiPpvFB7M4Z9l4yaip4k6gvSpL2mEMMs6sEXjqX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#C:\Users\CAIA84\Anaconda3\pkgs

#open/create a file to append data to
csvFile = open('twitter database.csv', 'a')

#use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q="#iphone",
                           count=100,
                           lang="en",
                           exclude_replies=True,
                           since="2018-01-01",
                           ).items(5000):
    # write a row to save tweets in the CSV file
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
    
csvFile.close()
    

# Open/create a file to append data to
csvFile = open('twitter database.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "google",
                           since = "2014-02-14",
                           until = "2014-02-15",
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()


dataset=pd.read_csv("C:\\Users\\DS7_RVepuri\\Desktop\\ML\\twitter database.csv")

