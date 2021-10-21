create_profile_table = """                
        CREATE TABLE IF NOT EXISTS profile ( 
                    id INTEGER UNIQUE NOT NULL, \
                    name VARCHAR(100),  \
                    screen_name VARCHAR(100), \
                    description TEXT, \
                    followers_count INTEGER, \
                    friends_count INTEGER, \
                    created_at TIMESTAMP);
        """
        

create_joe_biden_tweets_table = """CREATE TABLE IF NOT EXISTS joe_biden_tweets ( 
                        screen_name TEXT, \
                        id INTEGER NOT NULL, \ 
                        created_at TIMESTAMP,  \
                        full_text TEXT, \    
                        favorite_count INTEGER, \  
                        retweet_count INTEGER);"""