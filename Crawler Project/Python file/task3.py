import tweepy
from pandas.io.json import json_normalize
import sqlite3
import pandas as pd
import json
from tables import *
from tweepy.streaming import Stream
from column_names import task3_columns
from json_attributes import task3_lists

consumer_key = "hqpqsemDOOpW1uLUatxhF6dbH"
consumer_secret = "f6wbsfIsDGInCsBXDAFPjfMU2Zc5qT2nTZhHKmjUVMUOsm1RUB"

access_token = "1449802836942807051-FIT24Nh8Rb6P9f2AtpZodHtB7nyY7N"
access_token_secret = "oZOc0DfnDQHt7TJPfg7deNDa2ZsIuRlMXZTQ4YoFRiGju"

# Get Authorization to get use this API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


looping = True
list_to_dataframe = []

def keywords_search():
    # function document
    """To make a nest list to record every user's tweet content and other user info. by looping, and
        \nterminate this loop and transform them into dataframe to SQL\n\n
        First, there is a instruction to ask you to enter the username you want to query or to quit if you finish the\n
        checking\n\n
        1) type one name in each ask \n
        2) type the number of page (1 pages contains 20 tweets), you can set for 20-30 pages for 2 years ago and up to now
        3) Or type finish to call profile data execution\n
        Then your data is recorded in a database !!!!"""

    while looping:
        try:
            list_to_dataframe = []

            search_username = input("\nEnter keywords you want to search in the tweets "
                                    "\ne.g. COVID19 AND BNT, then type covid19, btn  (SEPARATE WITH A COMMA) a comma to between two keywords "
                                    "Otherwise, it will we treated as ONE WORD"
                                    "\n\ntype finish solely if you have finished typing:\t")
            if len(search_username) < 1:
                raise TypeError

            keyword_lists = search_username.strip().split(",")
            for i, keyword in enumerate(keyword_lists):
                keyword_lists[i] = keyword.strip()
            set(keyword_lists)  # Prevent duplicates keywords

            if search_username != "finish":
                page_num = int(input("Enter number of page you want to search from user's tweets:\t"))
                print("\n\nPlease wait for the finish (Speed depends on the pages you want to get)")

                for keyword in keyword_lists:
                    for pages in tweepy.Cursor(api.search_tweets, q=keyword).pages(page_num):
                        for page in pages:
                            each_tweet = []
                            json_string = json.dumps(page._json)
                            json_to_dictionary = json.loads(json_string)
                            flatten_json = pd.json_normalize(json_to_dictionary)

                            for element in task3_lists:
                                element = str(flatten_json[element][0])
                                each_tweet.append(element)
                            list_to_dataframe.append(each_tweet)
            else:
                conn = sqlite3.connect("project.db")  # connect to sqlite server and create database file
                cursor = conn.cursor()  # to execute query in Python

                cursor.execute(create_keyword_tweets_table)
                df = pd.DataFrame(list_to_dataframe, columns=task3_columns)
                df.to_sql("keyword_tweets", conn, if_exists="append", index=False)  # DataFrame to SQLite
                conn.commit()  # update data
                print("\nFinish !!!!  Please go to check your database file.")
                break

        except TypeError as e:
            print("\nPlease enter in a correct type")

        except tweepy.errors.NotFound as e:  # when username is not found
            print("User not found !!!")

        except tweepy.errors.Forbidden as e:
            print("User has been suspended ! ")  # when username is suspend






