# twitterASM
Twitter Crawler & SQL transformer 

ipynb可用 colab開  https://colab.research.google.com/notebooks/welcome.ipynb?hl=zh-tw
# This is a group project developed by:
  1. Jacky Cheung
  2. Ricky Chu
  3. Sam Wu

# The purpose of this project:

## Phase 1:
  1. Collect user's profile information from user -- JoeBiden   
            - user = api.get_user(screen_name = name)  
            
  2. Collect user's social network information from the Twitter user -- JoeBiden
            - for i, friend in enumerate(api.get_friends(screen_name=name)):
            - status = api.user_timeline(screen_name=name)  
            - other tweets that mentions about him
            - result = []
              for status in tweepy.Cursor(api.search_tweets, q=search).items(1000):
                   result.append(status)
                   
  3. Collect tweets with followings: ['Coronavirus', 'Vaccination']


## Phase 2: To SQL (SQLite: 
  1. Create & Design database
      - Table 1: Profile User
      - 
  3. INSERT DATA (keywords)  TO DATABASE &
  4. UPDATE DATA (keywords) & INSERT DATA TO DATABASE
