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
            - for i, friend in enumerate(api.get_friends(screen_name=name)) # 可有可無, 須考慮佢table 既存在有用不?  two columns in 1  table only?
                print(i, friend)
            - status = api.user_timeline(screen_name=name)  *** 有機會會遇到重覆既DATA (PROFILE), 要留意下。
            - other tweets that mentions about him
            - result = []
              for status in tweepy.Cursor(api.search_tweets, q=search).items(1000):
                   result.append(status)
                   
  3. Collect tweets with followings: ['Coronavirus', 'Vaccination']


## Phase 2: To SQL (SQLite: 
  1. Create & Design database
      - Table 1: user_profile                         - INSERT + UPDATE
      - Table 2: received_tweets                         - INSERT + UPDATE or (ON CONFLICTS, DO NOTHING)
      - Table 3: Specific Keyword Search              - INSERT + UPDATE or (ON CONFLICTS, DO NOTHING)
     
  3. INSERT DATA (keywords)  TO DATABASE &
  4. UPDATE DATA (keywords) & INSERT DATA TO DATABASE

TABLE 1:
CREATE TABLE user_profile (
        id PRIMARY KEY NOT NULL,
        name VARCHAR(100), 
        location VARCHAR(100),
        description TEXT,
        url (可有可無) TEXT,
        protected(* private/ public?) boolean,
        followers INTEGER,
        friends_count,
        created_at TIMESTAMP(* 不肯定),
        FAVORITE_COUNT INTEGER,
        verified boolean,
        statuses_count INTEGER);
        
        
table 2
CREATE TABLE received_tweets (
        created_at TIMESTAMP,
        tweet_content (text) TEXT,
        tweet_form (name) VARCHAR(100),
        protected boolean,
        followers_count INTEGER,
        friends_count INTEGER,
        
