import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect('twitter.db')
users = pd.read_csv('JoeBiden_tweets.csv')
# write the data to a sqlite table
users.to_sql('tweets', conn, if_exists='append', index = False)