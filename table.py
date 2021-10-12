table1 = """CREATE TABLE IF NOT EXISTS profile (
                    id INTEFER UNIQUE NOT NULL, \
                    name VARCHAR(100),  \
                    screen_name VARCHAR(100), \
                    location VARCHAR(100), \
                    description TEXT, \
                    url TEXT, \
                    protected TEXT, \
                    followers_count INTEGER, \
                    friends_count INTEGER, \
                    listed_count INTEGER, \
                    created_at TIMESTAMP, \
                    favourites_count INTEGER, \
                    statuses_count INTEGER);"""