import tweepy
import json
import sqlite3
from table import *
import pandas as pd


# use username to search his info. (Done!)
def scrap_info(name, api):            
    try:
        list_be_excluded = ["id_str", "entities", "geo", 
                            "coor", "coordinates", "place", 
                            "contributors", "status", "utc_offset",
                            "time_zone", "following", "follow_request_sent",
                            "notifications", "translator_type", "withheld_in_countries",
                            "contributors_enabled", "lang", "geo_enabled",
                            "verified"]
        user = api.get_user(screen_name = name)   

        # change into a more reable and managable json data
        str_ = json.dumps(user._json)
        dict_= json.loads(str_)
        for key, value in list(dict_.items()):
            if key in list_be_excluded or "profile" in key:
                dict_.pop(key)

            elif key.startswith("profile_") or key.startswith("is"):
                dict_.pop(key)

        df = pd.DataFrame.from_dict([dict_]) 
        df.to_csv ("C:\\Users\\123\Desktop\\twitterASM-kcwu\\data.csv", index = False, header=True)


        conn = sqlite3.connect("C:\\Users\\123\Desktop\\twitterASM-kcwu\\project_database") # change to 'sqlite:///your_filename.db'
        cur = conn.cursor()
        cur.execute(table1) # use your column names here
        df = pd.read_csv("C:\\Users\\123\Desktop\\twitterASM-kcwu\\data.csv")
        df.to_sql("profile", conn, if_exists='append', index=False)

    except sqlite3.IntegrityError as e:
        print("You have that data already, please go to check your data base!!!")
     

#  using username to search his tweets
def scrap_tweet(name, api):

    tweets = api.user_timeline(screen_name=name, count=2,
                               include_rts = False, tweet_mode = 'extended')

    for i in range(len(tweets)):
        included_list = ["created_at", "full_text", "entities", "extended_entities", "user", "is_quote_status", "retweet_count", "favorite_count", "lang"]
        print("\n\n")
        str_ = json.dumps(tweets[i]._json)
        dict_= json.loads(str_)
        for key, value in dict_.items():
            if key in included_list:
                print(f"{key}: {value}\n\n")