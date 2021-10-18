import json
import tweepy                         # Twitter API
from per_confidential import *        # Saving Token, Keys
import pandas as pd


# Ask for authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Activate API after authorization
api = tweepy.API(auth)


# Keywords on Coronavirus, Vaccination
keywords_search = ["coronavirus", "covid19", "covid-19", 
                    "bnt", "biotech", "moderna", 
                    "astrazeneca", "novavax", "sinovac"]

q_ = ' OR '.join(keywords_search)

date_since = "01-01-2019"
date_end = "18-10-2021"


tweets = api.search_tweets(keywords_search, count=200)

for search in tweets:
    lists = ["id", "created_at", "full_text", "entities", "favourites_count", "retweet_count"]
    dict_ = {"id": [], "created_at": [], "full_text": [], "entities": [], "favourites_count": [], "retweet_count": []}
    str_ = json.dumps(search._json)
    json_ = json.loads(str_)

    for list_ in lists:
        try:
            dict_[list_].append(json_[list_])

        except:
            pass

print(dict_)











