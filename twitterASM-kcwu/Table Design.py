SQL SERVER: SQLite

Step: API => Json => Pandas => SQL


""" 1. Profile Table """

CREATE TABLE IF NOT EXISTS profile ( 
                    id INTEGER UNIQUE NOT NULL, \
                    name VARCHAR(100),  \
                    screen_name VARCHAR(100), \
                    description TEXT, \
                    followers_count INTEGER, \
                    friends_count INTEGER, \
                    created_at TIMESTAMP, \
                    favourites_count INTEGER)

"""
Profile information
1. id --  Use as primary key to check for tweets in task 2 or 3

2. followers_count -- Is he famous/ popular?

3. favourites_count -- Is he famous/ popular?

4. friends_count  -- His relation network
"""

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  


""" 2. joe_biden_tweets """

CREATE TABLE IF NOT EXISTS joe_biden ( 
                        id INTEGER NOT NULL, \
                        created_at TIMESTAMP,  \
                        full_text TEXT, \
                        favorite_count INTEGER, \
                        retweet_count INTEGER)

"""
Tweets about Biden
1. id  -- foreign key to link with Profile Table  ----- maybe can scrape for the user who mentions about Joe Biden also 

2. created_at & favorite_count & retweet_count    ----- to see whether user is a bot or recently active only, and attitude on COVID-19 policy on Joe Biden  

3. full-text                                      ----- Maybe can be used for later stage for sentiment analysis for the COVID-19 policy on Joe Biden    
"""

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  


""" 3. keywords_tweets """

CREATE TABLE IF NOT EXISTS keywords_tweets ( 
                        id INTEGER NOT NULL, \
                        created_at TIMESTAMP,  \
                        full_text TEXT, \
                        entities TEXT, \
                        favourites_count INTEGER, \
                        retweet_count INTEGER) 

"""
Tweets about Biden
1. id  -- foreign key to link with Profile Table  ----- maybe can scrape for the user who mentions about Joe Biden also 

2. created_at & favorite_count & retweet_count    ----- to see whether user is a bot or recently active only, and attitude and concern on vaccination/ COVID-19

3. full-text                                      ----- Maybe can be used for later stage for sentiment analysis for the COVID-19 policy on Joe Biden and WHO 
                                                            their promotion and sense, and understanding of precautionary issues
"""
