import pandas as pd
import numpy as np
import re
import codecs
import json
import tweepy
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib

# Assign the Sentiment Intensity Analyzer to analyser
analyser = SentimentIntensityAnalyzer()

# Test out analyser example one
analyser.polarity_scores("The movie is good")

# Test out analyser example two
analyser.polarity_scores("The movie is very bad")


# Compound score has a range of [-1, 1], being:
# [-1 to 0): negative,
# [0]: neutral
# (0 to +1]: positive

def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1

# Test
sentiment_analyzer_scores('The movie is long!!!')

# Test
#sentiment_analyzer_scores('The movie is VERY Good!!!!')
#analyser.polarity_scores('The movie is VERY Good!!!!')

# Import Google Translator to translate in any language

from googletrans import Translator
translator = Translator()

# Testing translator works

translator.translate('hola, todo bien?').text

# Analyzing translated text

text = translator.translate('la pelicula es mala').text
analyser.polarity_scores(text)

# Adding translate to the analyzer function
#so we can perform sentiment analysis in any language



def sentiment_analyzer_scores(text, engl=True):
    if engl:
        trans = text
    else:
        trans = translator.translate(text).text
    score = analyser.polarity_scores(trans)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1


# Testing function sentiment_analyzer_scores

#text = 'o dia esta lindo, com muito sol'
#sentiment_analyzer_scores(text, False)

# Passing in Twitter Authentication
# Use fresh keys regenerated by Twitter Dev account to avoid errors

consumer_key = 'dDtx01x3da8O4D2iqEunv8ACW'
consumer_secret = 'B3jzCGnENSATdupmLEi3gSxX9sRhspwth7zmO4VSIf0YzGehsM'
access_token = '33548073-WXeW7OjY1aKtq8GIeUc9w0E1U3x0cSix0lIeUymhe'
access_token_secret = 'Bn7PDOGHw938QYZK7bLL8OXWNmoKQZg7nDwOHOwXOyKUK'

# Using Tweepy for creating a persistent connection to Twitter
# Reading each incoming tweet
# Fault tolerance

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Save tweets as a dataset as a list for future analysis


def list_tweets(user_id, count, prt=False):
    tweets = api.user_timeline(
        "@" + user_id, count=count, tweet_mode='extended')
    tw = []
    for t in tweets:
        tw.append(t.full_text)
        if prt:
            print(t.full_text)
            print()
    return tw


# Need to clean tweets for sentiment analysis

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

def clean_tweets(lst):
    # remove twitter Re-tweet handles (RT @xxx:)
    lst = np.vectorize(remove_pattern)(lst, "RT @[\w]*:")
    # remove twitter handles (@xxx)
    lst = np.vectorize(remove_pattern)(lst, "@[\w]*")
    # remove URL links (httpxxx)
    lst = np.vectorize(remove_pattern)(lst, "https?://[A-Za-z0-9./]*")
    # remove special characters, numbers, punctuations (except for #)
    lst = np.core.defchararray.replace(lst, "[^a-zA-Z#]", " ")
    return lst

# 200 Tweets sent by Trump for sentiment analysis, loaded in a list tw_trump

user_id = "realDonaldTrump"
count=200
tw_trump = list_tweets(user_id, count)

# indexing into list at the 10th tweet

tw_trump[10]

# Sentiment analysis for Trump Tweet

sentiment_analyzer_scores(tw_trump[100])


# Define function anl_tweets for analyzing twitter sentiment
# and plotting the sentiments, categorized in 3 categories

def anl_tweets(lst, title='Tweets Sentiment', engl=True ):
    sents = []
    for tw in lst:
        try:
            st = sentiment_analyzer_scores(tw, engl)
            sents.append(st)
        except:
            sents.append(0)
    ax = sns.distplot(
        sents,
        kde=False,
        bins=3)
    ax.set(xlabel='Negative                Neutral                 Positive',
           ylabel='#Tweets',
          title="Tweets of @"+title)
    return sents

# Plot to display sentiments in the last 200 odd tweets

tw_trump_sent = anl_tweets(tw_trump, user_id)