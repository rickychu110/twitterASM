# twitterASM
Twitter Crawler & SQL transformer 
outlook email
ID:genrickylearn2021@outlook.com
PW:Genhk1234

## Project Briefing and Team Formation
  #### 1.Jacky Cheung
  #### 2.Ricky Chu
  #### 3.Sam Wu



# Goal: Build Twitter data crawler   -- for later analysis

## Bridging Python and SQL programming knowledge with Project
#### 1. ETL techiques
#### 2. Pipeline
#### 3. SQL Query
#### 4. API




## Mission & define tasks:      Collect...

###   1. @JoeBiden's profile 
###   2. @JoeBiden's social network information
###   3. tweets with keywords: ['Coronavirus', 'Vaccination']


# Values:
### - Whats is it worthy?
### 1. User:
### Designed for
#### - A) [political party]: Political orientation  ---- election 
#### - B) [Statistic analyst]:  1. Medical issue (how the content of tweet affects the medical issue) 2.sense of covid precautionary
#### - C) [government/marketing expertise]: understand mainstream issue then make certain policies & solution
#### - D) [general public]: recording 




## 1. Tweepy:       ---     Data extraction
### Why tweepy but not other?
#### - Official -- secure
#### - Convenient to use
#### - Free
#### - Authorized

## 2. Panadas    ----  Data Tranformation
### Why Panadas? 
#### - Convenient to use -- Easy to USE
#### - Supportiver in mult-style transformation


## 3. SQLite:    ----  Data Load
### Why SQLite? 
#### - Built-in function -- convenient to use
#### - Convenient to use -- Easy to USE
#### - More comprehensive than other SQL tools -- for our group:) 


# 2. Brainstorming
# - Phase 1: Data collection  (4-5 days)


####   1. @JoeBiden's profile   tweepy user  

####   2. @JoeBiden's social network information  (a)

####   3. tweets with keywords: ['Coronavirus', 'Vaccination']


# - Phase 2: Import Data to SQL (8-9 days)


### Transform data and send to SQL:
1. Profile -- can over write
table1.1:  profile 
        1. id, 
        2. location, 
        3. description,
        4. url,
        5. protected TEXT, 
        6. followers_count,
        7. friends_count INTEGER,
        8. listed_count INTEGER,
        9. created_at TIMESTAMP,
        10. favourites_count INTEGER,
        11. statuses_count INTEGER
           
2. Who_care_JoeBiden(Joe Biden) -- cannot overwrite
### table2 = trace_target
         1. user_info,
         2. id,
         3. created_at,
         4. full_text,
         5. entities['hashtags'],
         6. entities['user_mentions'],
         7. favourites_count,
         8. retweet_count,
         9. favorite_count,
         10.lang
           

### Vaccines
BioNTech
Moderna
Johnson & Johnson's Janssen
mRNA Vaccines
Vector Vaccines
...

### Coronavirus
COVID-19
COVID19
COVID-19 Coronavirus
...

### Time-frame

3. Tweet Table (COVID19, )
table3 = kwyword_search,
         1. user_info,
         2. id,
         3. created_at,
         4. full_text,
         5. entities['hashtags'],
         6. entities['user_mentions'],
         7. favourites_count,
         8. retweet_count,
         9. favorite_count,
         10.lang
           
           
                 
# Flow design

![Opportunity Solution Tree Template(1).jpg](attachment:73e268bd-4a0e-4690-98fa-a5485ee22852.jpg)
