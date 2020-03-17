# -*- coding: utf-8 -*-

    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vaderSentiment
analyser = SentimentIntensityAnalyzer
def emotionalanalysis():
    file= input('Enter file name: ')
    with open(file, 'r',encoding='utf-8-sig') as f:
          mylist=list(f)
          for line in mylist:
              analysing= analyser.polarity_scores(line)
              print("{:-<00} {}".format(line, str(analysing)))

#can run emotional analysis using vader for our tweets to see the positivity or negativity of them

emotionalanalysis()
