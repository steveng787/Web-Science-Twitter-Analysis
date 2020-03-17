# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 05:25:23 2020

@author: stevi
"""

import json
import tweepy
import csv
import re
from autocorrect import Speller
check=Speller(lang='en')
import pandas as pd
from Main import twitter_cred
from contractions_in_tweets import expand_contractions
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vader sentiment 
analyser = SentimentIntensityAnalyzer()
from emoji import UNICODE_EMOJI #pip install emoji

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
    

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
consumer_key = info['CONSUMER_KEY']
consumer_secret = info['CONSUMER_SECRET']
access_key = info['ACCESS_KEY']
access_secret = info['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
def csvhashtag(hashtag,emotion):
    for tweet in tweepy.Cursor(api.search, q='-filter:retweets -filter:mentions -filter:quotes -filter:links ' + hashtag ,rpp=150,lang="en",wait_on_rate_limit=True,tweet_mode="extended").items(300):
                                hashtags=0
                                emojis=0
                                tweet.full_text.replace('\n',' ')
                                for i in tweet.full_text:
                                    if i == "#":
                                        hashtags= hashtags +1 
                                    if i == i in UNICODE_EMOJI:
                                        emojis=emojis+1 
                                   
                                if hashtags <3: #removing tweets with more than 3 hashtags
                                    if emojis <3: #removing tweets with more than 3 emojis
                                        with open(emotion + '.csv', 'a', encoding='utf-8-sig',errors='ignore') as the_file:
                                            csvWriter=csv.writer(the_file)
                                            if analyser.polarity_scores(emotion+'.csv'[3])['compound'] <= abs(0.1):
                                                csvWriter.writerow([tweet.created_at, tweet.id_str, tweet.full_text, expand_contractions(check(re.sub(r'(.)\1+', r'\1\1',str(tweet.full_text.lower()) + '\n'))),emotion])
#using regex i removed any letters that were duplicated more than twice, eg haaapppppppyyyyyyyy is now just haappyy.


def csvemoji(emoji,emotion):
    for tweet in tweepy.Cursor(api.search, q='-filter:retweets -filter:mentions -filter:quotes -filter:links ' + emoji ,rpp=150,lang="en",wait_on_rate_limit=True,tweet_mode="extended").items(120):
                                hashtags=0
                                emojis=0
                                tweet.full_text.replace('\n',' ')
                                for i in tweet.full_text:
                                    if i == "#":
                                        hashtags= hashtags +1 
                                    if i == i in UNICODE_EMOJI:
                                        emojis=emojis+1
                                if hashtags <3: 
                                    if emojis <3:
                                            with open(emotion + '.csv', 'a', encoding='utf-8-sig',errors='ignore') as the_file:
                                                csvWriter=csv.writer(the_file)
                                                if analyser.polarity_scores(emotion+'.csv'[3])['compound'] <= abs(0.1):
                                                    csvWriter.writerow([tweet.created_at, tweet.id_str, tweet.full_text, expand_contractions(check(re.sub(r'(.)\1+', r'\1\1',str(tweet.full_text.lower()) + '\n'))),emotion])
                                        
def remove_contractions_and_letters(emotion):
    hashtags=0
    for i in emotion + '.csv':
         if i == "#":
             hashtags= hashtags +1 
    if hashtags <3:
            df = pd.read_csv(emotion + '.csv', encoding='utf-8-sig')
            expand_contractions(check(re.sub(r'(.)\1+', r'\1\1',str(df))))
            df.to_csv('final_' + emotion +'.csv',encoding='utf-8-sig',  index=False)

def duplicateremoval(emotion):
    df = pd.read_csv(emotion + '.csv', encoding='utf-8-sig')
    df.drop_duplicates(subset=[df.columns[2],df.columns[3]],inplace=True,keep="first")
    df.to_csv('final_' + emotion +'.csv',encoding='utf-8-sig',  index=False)
    #removing duplicates using pandas
    
def removevader(emotion):
    with open('The_final_' +emotion +'.csv', 'w', newline='', encoding='utf-8-sig') as outcsv:
        writer=csv.writer(outcsv)
        with open('final_' + emotion + '.csv', 'r', encoding='utf-8-sig',errors='ignore') as f:
            reader=list(csv.reader(f))
            for row in reader: 
                scores=analyser.polarity_scores(row)
                if scores['compound'] >= abs(-0.05):
                    writer.writerow(row for row in reader)
                  
def combinefiles():
    with open('combined_file.csv', 'w', newline='',encoding='utf-8-sig') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Date", "Tweet id", "Uncleaned Data", "Cleaned Data", "Class"])

        with open('final_excited.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)

        with open('final_happy.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)
        with open('final_pleasant.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)
        with open('final_sad.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)
        with open('final_fear.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)
        with open('final_angry.csv', 'r', newline='',encoding='utf-8-sig') as incsv:
            reader = csv.reader(incsv)
            writer.writerows(row for row in reader)
            #combining our files
            









def searchfortweets():
    emoji= "🤩 OR 🤪 OR 🤗"
    emotion="excited"
    hashtag="#excited OR #excited"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)

    hashtag="#happy OR #happiness OR #love"
    emotion="happy"
    emoji="🙂 OR 😀 OR 😌 OR ☺️"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)

    emoji= "😌"
    hashtag="#pleasant OR #delightful OR #good"
    emotion="pleasant"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)

    emoji="😔 OR 😭 OR 😞"
    hashtag="#sad OR #sadness OR #depression"
    emotion="sad"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)

    emoji= "😨 OR 😱 OR 😰"
    hashtag= "#fear OR #scary OR #fright OR #horror OR #anxiety"
    emotion="fear"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)
    
    emoji= "😠 OR 👿 OR 😡"
    hashtag= "#angry OR #anger"
    emotion="angry"
    csvhashtag(hashtag,emotion)
    csvemoji(emoji,emotion)
    duplicateremoval(emotion)
    
    combinefiles()

#searching for the tweets




