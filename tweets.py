import json
import tweepy
import sqlite3
import pandas as pd

consumer_key = "M7NS5nExt5tyfFA0dGL65KHyU"
consumer_secret = "CmGwDXv6WvM79dkKIx1UZwE15YJI532ktCBXq3zMX1Azfe7JFj"

access_token = "3039143238-K3GIEUOMM13dC1vjdvXJMSgz9289ncF3mgDapZb"
access_token_secret = "mwXNcK8OUX4Uxx5aNRqGEk28A1P5OjExvHOuoxApGohsF"

BEAR_TOKEN ="AAAAAAAAAAAAAAAAAAAAAJJOUgEAAAAAhoFc8pc2lrrM5MXowXeW%2BmTKht0%3D5gbSSX0MB3fuGQ18FSiREkfKGyOvwVVHzgqCFdAwWjypLXHbyK"

auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user(screen_name = "JoeBiden",include_entities=False)
print("id: " + str(user.id))
print("id_str: " + user.id_str)
print("name: " + user.name)
print("screen_name: " + user.screen_name)
print("location: " + str(user.location))
print("profile_location: " + str(user.profile_location))
print("description: " + user.description)
print("\n")

tweets=api.user_timeline(
    screen_name="JoeBiden",
    count=5,
    include_rts=False,
    tweet_mode="extended"
)

for info in tweets[:3]:
    print("ID:{}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")

#下面未用到啦
all_tweets = []
all_tweets.extend(tweets)
outputtweets=[[tweets.id_str, 
              tweets.created_at, 
              tweets.favorite_count, 
              tweets.retweet_count, 
              tweets.full_text.encode("utf-8").decode("utf-8")] 
             for idx,tweet in enumerate(all_tweets)]
df = pd.DataFrame(outputtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
df.to_csv('%s_tweets.csv' % "JoeBiden",index=False)
df.head(3)
