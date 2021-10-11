import tweepy
import json
from per_confidential import *


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Variable         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# Ask for authorization
auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Activate API after authorization
api = tweepy.API(auth)


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Method 1         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# use username to search his info.
def scrap_info(name):
    user = api.get_user(screen_name = name)   

    """ turn output into more readable json string:  
       
    class object --> json string --> dict  """

    json_str = json.dumps(user._json)  
    profile_dict = json.loads(json_str)

    print(f"Profile information of {name} is:\n")
    count = 0
    for key, value in profile_dict.items():
        # Separating data        
        # Unpack the nest dictionies
        
        if key == "status":   
            status_dict = profile_dict[key]
            for key1, value1 in status_dict.items():
                print(f"{key1}: {value1}")
                count += 1

                if count % 5 == 0:
                    print("\n")

        # Unpack the nest dictionies
        elif key == "entities":
            entities_dict = profile_dict[key]
            for k1, v1 in entities_dict.items():
                print(f"{k1}: {v1}")
                count += 1
                if count % 5 == 0:
                    print("\n")
        
        else:
            print(f"{key}: {value}")
            count += 1


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Method 2         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """   

#  using username to search his tweets
def scrap_tweet(name):
    status = api.user_timeline(screen_name=name) 
    print("\n\n\n")

    for i in range(1):
        msg = json.dumps(status[i-1]._json)  
        for key, value in json.loads(msg).items():
            print(f"{key}: {value}")


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Method 3        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

 # use username to search his networks (max= 20)
def frd_list(name):
    print(f"\n\n\nThe latest 20 friends of {name} are:\t\n")
    for i, friend in enumerate(api.get_friends(screen_name=name)):
        print(f"{i+1}. {friend.screen_name}")       # Order starts from 1