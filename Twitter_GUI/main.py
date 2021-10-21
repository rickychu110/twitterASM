from urllib.parse import uses_relative
from twitter_gui_login import Twitter_Crawler_login_menu
from twitter_gui_page1 import Twitter_Crawler_page1
import tweepy
from tables import *


# Login
login = Twitter_Crawler_login_menu()

#Auth
auth = tweepy.OAuthHandler(login.consumer_key, login.consumer_secret)
auth.set_access_token(login.access_token, login.access_token_secret)

# page1 
p1 = Twitter_Crawler_page1(tweepy.OAuthHandler(login.consumer_key, login.consumer_secret), tweepy.API(auth))


# page2
#p1 = Twitter_Crawler_page2()
