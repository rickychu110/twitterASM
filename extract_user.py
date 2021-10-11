import tweepy
import json

# use username to search his info.
def scrap_info(name, api):              
    list_be_excluded = ["id_str", "entities", "geo", 
                        "coor", "coordinates", "place", 
                        "contributors", "status", "utc_offset",
                        "time_zone", "following", "follow_request_sent",
                        "notifications", "translator_type", "withheld_in_countries"]
    user = api.get_user(screen_name = name)   

    # change into a more reable and managable json data
    json_str = json.dumps(user._json)  
    profile_dict = json.loads(json_str)

    print(f"Profile information of {name} is:\n")
    for key, value in profile_dict.items():      
        if "profile_" in key:
            continue
        if key not in list_be_excluded:
            print(f"{key}: {value}")
    print("\n\n\n\n\n\n\n\n")


#  using username to search his tweets
def scrap_tweet(name,api):

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