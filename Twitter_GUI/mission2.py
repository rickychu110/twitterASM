import tweepy
from per_confidential import *        # Saving Token, Keys
from pandas.io.json import json_normalize
import json
import sqlite3
import pandas as pd
from tables import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def scrap_tweet(name):
    tweets = api.user_timeline(screen_name=name, count=1000, tweet_mode='extended')

    items = ["id", "created_at", "full_text",
             "favorite_count", "retweet_count"]
    col_names = {"id": [], "created_at": [], "full_text": [],
             "favorite_count": [], "retweet_count": []}
    
    for tweet in tweets:
        print(tweet)
        str_ = json.dumps(tweet._json)
        json_ = json.loads(str_)
        for item in items:
            col_names[item].append(json_[item])
            col_names

    df = pd.DataFrame(col_names)

    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    
    cursor.execute(create_joe_biden_tweets_table)
    conn.commit()

    df.to_sql("joe_biden_tweets", conn, if_exists='replace', index=False)
    print("Finish !!!")
    

scrap_tweet("joebiden")