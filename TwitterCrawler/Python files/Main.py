# -*- coding: utf-8 -*-

import json
import tweepy #pip install tweepy
from autocorrect import Speller
import re
check=Speller(lang='en')
from Constructions import contractions
# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'kPsRkyMWW3hnaN7wexa3H1gLe'
twitter_cred['CONSUMER_SECRET'] = '4dKxfm60k616xifuBZF4QRncxo4ugTWAEt9KsQyYiRNO9bYdMF'
twitter_cred['ACCESS_KEY'] = '3319034476-3N39BrUKOz5xlRYurLOhrQBa6TArTmPPhtoFBcD'
twitter_cred['ACCESS_SECRET'] = '74hrAUcqOQWAGlIiF8oX9OiMDjnfof6V2EVnoLoaupJw5'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
    

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
consumer_key = info['CONSUMER_KEY']
consumer_secret = info['CONSUMER_SECRET']
access_key = info['ACCESS_KEY']
access_secret = info['ACCESS_SECRET']

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the hashtag that you want to look out for


#using regex i removed any letters that were duplicated more than twice, eg haaapppppppyyyyyyyy is now just haappyy.


contractions_re = re.compile('(%s)' % '|'.join(contractions.keys()))
def expand_contractions(s, contractions=contractions):
    def replace(match):
        return contractions[match.group(0)]
    return contractions_re.sub(replace, s)
    #replaces any can't etc with the fully expressed version eg. can not. Also have added common shorthand problems to this such as OMG and LOL
    
    

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


