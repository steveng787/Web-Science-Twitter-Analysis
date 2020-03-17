# -*- coding: utf-8 -*-
import tweepy
import json
import tweepy
import csv
import re
from autocorrect import Speller
check=Speller(lang='en')
import numpy as np
import pandas as pd
def removelettersintweets(hashtag):
    for tweet in tweepy.Cursor(api.search, q='#' + hashtag,rpp=150,lang="en",wait_on_rate_limit=True).items(50):
                               with open("#" + hashtag + '.txt', 'a') as \
                                         the_file:
                                             the_file.write(check(re.sub(r'(.)\1+', r'\1\1',str(tweet.text.encode('utf-8')) + '\n')))
#using regex i removed any letters that were duplicated more than twice, eg haaapppppppyyyyyyyy is now just haappyy.
print(check(re.sub(r'(.)\1+', r'\1\1',"happpppppppppppppppyyyyyyyyyyyyyyyyyyyyyy, heyyyyyyyy, loooooooove")))