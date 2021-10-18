import tweepy   
from per_confidential import *        # Saving Token, Keys
import sqlite3
import pandas as pd
import json


# Get Authorization to get use this API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# scrap for info for Joe Biden
def scrap_info(name):
    try:
        data_dict = {}   # Create dict to tranform into DataFrame
        lists = ["id", "name", "screen_name",
                "description", "followers_count", "friends_count",
                 "created_at", "favourites_count"]


        user = api.get_user(screen_name=name)     # get info from profile
        str_ = json.dumps(user._json)             # Json to string
        json_ = json.loads(str_)                  # String to dict property

        for list in lists:
            data_dict[list] = json_[list]         

        conn = sqlite3.connect('project.db')      # connect to sqlite server and create database file
        cursor = conn.cursor()                    # to execute query in Python

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

        df = pd.DataFrame([data_dict])            # Dict to dataframe
        df.to_sql("profile", conn, if_exists='replace', index=False)    # DataFrame to SQLite
        print("Finish !!!")

    except sqlite3.IntegrityError:                # If duplicate, raise error to signal that you already have this data
        print("You have already get this data!!!")

scrap_info("@joebiden")
