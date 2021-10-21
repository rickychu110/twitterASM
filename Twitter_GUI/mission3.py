import json
import tweepy                         # Twitter API
from per_confidential import *        # Saving Token, Keys
import pandas as pd
import sqlite3


# Ask for authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Activate API after authorization
api = tweepy.API(auth)



def keywords_search(keywords_lists):
# Keywords on Coronavirus, Vaccination
    quote = ' OR '.join(keywords_lists)
    tweets = api.search_tweets(quote, count=200)

    for tweet in tweets:
        lists = ["id", "created_at", "full_text", "favourites_count", "retweet_count"]
        dict_ = {}
        list_ = []
        str_ = json.dumps(tweet._json)
        json_ = json.loads(str_)

        for item in lists:
            try:
                dict_[item] = (json_[item])

            except:
                dict_[item] = " "
            
            finally:
                list_.append(dict_)

    df = pd.DataFrame(list_)

    conn = sqlite3.connect('project.db')      # connect to sqlite server and create database file
    cursor = conn.cursor()                    # to execute query in Python

    create_keywords_tweets_table = """CREATE TABLE IF NOT EXISTS keywords_tweets ( 
                        id INTEGER NOT NULL, \
                        created_at TIMESTAMP,  \
                        full_text TEXT, \
                        favourites_count INTEGER, \
                        retweet_count INTEGER);"""

    cursor.execute(create_keywords_tweets_table)
    conn.commit()

    df.to_sql("keywords_tweets", conn, if_exists='replace', index=False)    # DataFrame to SQLite
    print("Finish !!!")



keywords = ["coronavirus", "covid19", "covid-19", 
                        "bnt", "biotech", "moderna", 
                        "astrazeneca", "novavax", "sinovac"]

keywords_search(keywords)







