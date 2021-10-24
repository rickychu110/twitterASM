import tweepy
from pandas.io.json import json_normalize
import sqlite3
import pandas as pd
import json
from tables import *
import tweepy
from json_attributes import task2_lists
from column_names import task2_columns

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

# PAST TWEET CONTENT
def search_user_past_tweets():
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
        count = 0
        try:
            search_username = input("\nEnter screen name (e.g. @happy), or finish if you have done typing:\t").lower()
            if search_username != "finish":
                page_num = int(input("Enter number of page you want to search from user's tweets:\t"))
                print("\n\nPlease wait for the finish (Speed depends on the pages you want to get)")

                for pages in tweepy.Cursor(api.user_timeline, screen_name=search_username).pages(page_num):
                    # make searching attributes in json become more sufficient
                    for page in pages:
                        each_tweet = []
                        json_string = json.dumps(page._json)
                        json_to_dictionary = json.loads(json_string)
                        flatten_json = pd.json_normalize(json_to_dictionary)

                        for element in task2_lists:
                            element = str(flatten_json[element][0])
                            each_tweet.append(element)

                        list_to_dataframe.append(each_tweet)
                        count += 1

            else:
                conn = sqlite3.connect('project.db')  # connect to sqlite server and create database file
                cursor = conn.cursor()  # to execute query in Python

                #time baseline to compare with stream listener in time to record the trend e.g. followers_count
                cursor.execute(create_joe_biden_tweets_table)
                df = pd.DataFrame(list_to_dataframe, columns=task2_columns)
                df.to_sql("joe_biden_tweets", conn, if_exists="append", index=False)  # DataFrame to SQLite
                conn.commit()  # update data
                print("\nFinish !!!!  Please go to check your database file.")
                break


        except TypeError as e:
            print("\nPlease enter the answer in a correct type: number !!!!")

        except tweepy.errors.NotFound as e:  # when username is not found
            print("User not found !!!")

        except tweepy.errors.Forbidden as e:
            print("User has been suspended ! ")  # when username is suspend






