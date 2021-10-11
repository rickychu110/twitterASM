from per_confidential import *        # Saving Token, Keys
from extract_user import *            # functions being import to use
import tweepy                         # Twitter API
import json                           # change format


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Variable         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# Ask for authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Activate API after authorization
api = tweepy.API(auth)


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Method           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

def keyword_search():
    for search in ["Coronavirus", "Vaccination"]: 

        # Search keywords from tweets for 1000 times (amount is changable):

        searched_tweets = [status for status in tweepy.Cursor(api.search_tweets, q=search).items(10)]

        for i in range(len(searched_tweets)):

            # class obj --> json string --> json format(similar to dict)
            json_str = json.dumps(searched_tweets[i-1]._json)
            result_dict = json.loads(json_str)

            # make it easy to read
            for key, value in result_dict.items():
                print(f"{key}: {value}")
