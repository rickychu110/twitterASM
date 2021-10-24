import tweepy   
import sqlite3
import pandas as pd
import json
import time
from tables import *
from json_attributes import task1_lists
from column_names import task1_columns

consumer_key = "hqpqsemDOOpW1uLUatxhF6dbH"
consumer_secret = "f6wbsfIsDGInCsBXDAFPjfMU2Zc5qT2nTZhHKmjUVMUOsm1RUB"

access_token = "1449802836942807051-FIT24Nh8Rb6P9f2AtpZodHtB7nyY7N"
access_token_secret = "oZOc0DfnDQHt7TJPfg7deNDa2ZsIuRlMXZTQ4YoFRiGju"

# Get Authorization to get use this API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# make column name in dataFrame
def scrap_info():
    # function document
    """To make a nest list to record every user's profile data by looping, and
    \nterminate this loop and transform them into dataframe to SQL\n\n
    First, there is a instruction to ask you to enter the username you want to query or to quit if you finish the\n
    checking\n\n
    1) type one name in each ask \n
    2) Or type finish to call profile data execution\n
    Then your data is recorded in a database !!!!"""

    looping = True
    list_to_dataframe = []
    while looping:
        # Allow the user to custom the user they want to find
        list_for_each_user = []
        search_username = input("Enter the user name (e.g. @happy, or type finish if you want to end this search):\t")

        if search_username.lower() == "finish":    # if stop, then transform list to dataframe and send to sql
            conn = sqlite3.connect('project.db')  # connect to sqlite server and create database file
            cursor = conn.cursor()  # to execute query in Python

            # time baseline to compare with stream listener in time to record the trend e.g. followers_count
            cursor.execute(create_profile_table)

            df = pd.DataFrame(list_to_dataframe, columns=task1_columns)

            # DataFrame to SQLite (append new data in an existed but not overwrite all data)
            df.to_sql("profile", conn, if_exists='append', index=False)
            conn.commit()  # update data
            print("Finish !!!!  Please go to check your database file.")
            break

        else:
            try:
                user = api.get_user(screen_name=search_username)  # profile data extraction
        
                json_string = json.dumps(user._json)             # Json to String
                json_to_dictionary = json.loads(json_string)     # String to Dictionary: easy to get values

                for element in task1_lists:
                    if element == "scrap_time":
                        list_for_each_user.append(time.strftime("%a %d %b %Y %H:%M:%S"))
                    else:
                        list_for_each_user.append(json_to_dictionary[element])  # extract json_to_dictionary value and put into list
                list_to_dataframe.append(list_for_each_user)

            except tweepy.errors.NotFound as e:    # when username is not found
                print("User not found !!!")

            except tweepy.errors.Forbidden as e:
                print("User has been suspended ! ")   # when username is suspend
