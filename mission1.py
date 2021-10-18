import tweepy
from per_confidential import *        # Saving Token, Keys
import sqlite3
import pandas as pd
import json


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def scrap_info(name):
    try:
        data_dict = {}
        lists = ["id", "name", "screen_name",
                "description", "followers_count", "friends_count",
                 "created_at", "favourites_count"]

        user = api.get_user(screen_name=name)
        str_ = json.dumps(user._json)
        json_ = json.loads(str_)

        for list in lists:
            data_dict[list] = json_[list]

        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        create_profile_table = """CREATE TABLE IF NOT EXISTS profile ( 
                    id INTEGER UNIQUE NOT NULL, \
                    name VARCHAR(100),  \
                    screen_name VARCHAR(100), \
                    description TEXT, \
                    followers_count INTEGER, \
                    friends_count INTEGER, \
                    created_at TIMESTAMP, \
                    favourites_count INTEGER);"""

        cursor.execute(create_profile_table)
        conn.commit()

        df = pd.DataFrame([data_dict])
        df.to_sql("profile", conn, if_exists='replace', index=False)
        print("Finish !!!")

    except sqlite3.IntegrityError:
        print("You have already get this data!!!")


scrap_info("@joebiden")
