import tweepy
from per_confidential import *        # Saving Token, Keys
from pandas.io.json import json_normalize
import json
import sqlite3
import pandas as pd


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def scrap_tweet(name):
    tweets = api.user_timeline(screen_name=name, count=10, tweet_mode='extended')
    items = ["id", "created_at", "full_text",
             "favorite_count", "retweet_count"]
    col_names = {"id": [], "created_at": [], "full_text": [],
             "favorite_count": [], "retweet_count": []}

    for tweet in tweets:
        str_ = json.dumps(tweet._json)
        json_ = json.loads(str_)
        for item in items:
            col_names[item].append(json_[item])

    df = pd.DataFrame(col_names)

    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    create_profile_table = """CREATE TABLE IF NOT EXISTS joe_biden_tweets ( 
                        id INTEGER NOT NULL, \
                        created_at TIMESTAMP,  \
                        full_text TEXT, \
                        favorite_count INTEGER, \
                        retweet_count INTEGER);"""

    cursor.execute(create_profile_table)
    conn.commit()

    df.to_sql("joe_biden_tweets", conn, if_exists='replace', index=False)
    print("Finish !!!")

scrap_tweet("joebiden")