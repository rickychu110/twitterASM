import tweepy   
from per_confidential import *        # Saving Token, Keys
import sqlite3
import pandas as pd
import json
import time
from tables import *

# Get Authorization to get use this API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# scrap for info for Joe Biden
def scrap_info(name):
    try:
        data_dict = {}   # Create dict to tranform into DataFrame
        lists = ["id", "name", "screen_name", "description", 
                 "followers_count", "friends_count", "created_at"]


        user = api.get_user(screen_name=name)     # get info from profile
 
        str_ = json.dumps(user._json)             # Json to string
        json_ = json.loads(str_)                  # String to dict property

        for list in lists:
            data_dict[list] = json_[list]         

        conn = sqlite3.connect('project.db')      # connect to sqlite server and create database file
        cursor = conn.cursor()                    # to execute query in Python

        
        # COLLECT DATATIME -- FOR COMPARASION
        print(time.strftime("%a %d %b %Y %H:%M:%S"))
        # 時區問題未解決


        # not change 
        cursor.execute(create_profile_table)
        conn.commit()   # update data 

        df = pd.DataFrame([data_dict])            # Dict to dataframe
        df.to_sql("profile", conn, if_exists='replace', index=False)    # DataFrame to SQLite
        print("Finish !!!")

    except sqlite3.IntegrityError:                # If duplicate, raise error to signal that you already have this data
        print("You have already get this data!!!")

scrap_info("@joebiden")
