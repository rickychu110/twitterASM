import tweepy                         # Twitter API
from per_confidential import *        # Saving Token, Keys
from extract_user import *            # Functions being import to use (Phase 1)
from keyword_search import *          # Functions being import to use (Phase 1)


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Variable         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# Ask for authorization
auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Activate API after authorization
api = tweepy.API(auth)


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Method 1         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

def main():
    """ 
    Welcome to this twitter crawler ๐ !!!  You can obtain two main services in this tool:
       1. Scraping on twitter user's profile ๐ต๏ธโโ๏ธ and his relationship network ๐จโ๐จโ๐งโ๐ง;
       2. Search for key words ๐งโ๐ณ

    To use this machine, first, choose for mode you want to use:
        For mode 1, enter the username you are looking for, and wait for the result ๐ค๐ผ.  
        For mode 2, the keywords are entered as default so wait for the result ๐ค๐ผ.

    Thank you :)

    """

    # Mode 1: Getting user profile, relationship network

    while True: 
        mode = input("\n\n\nWhich mode would you like to pick? (1 or 2 or quit)\t").lower()
        if  mode == "1":
            try:
                name = input("Give me username, and get the data.\t").lower()
                scrap_info(name)
                scrap_tweet(name)
                frd_list(name)

            except NameError as e:
                print("Incorrect username!! Try again later.")

            finally:
                print("\n\nThe crawler is executed!")


        # Mode 2:  Search keywords
        elif mode == "2":
            keyword_search()


        elif mode == "quit":
            print("See You!!")
            break

        else:
            print("Sorry, try again!!")


"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        Main Method Call         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# only execute when it is run as main.py
if __name__ == "__main__":
    print(main.__doc__)
    main()
