from task1 import scrap_info
from task2 import search_user_past_tweets
from task3 import keywords_search

def main():
    loop = True
    # Let user to pick services
    while loop:
        ask = input("\n\nWelcome to use this crawler, please choose the function"
                    "1) User's profile checking, please type 1\n"
                    "2) User's tweet checking, please type 2\n"
                    "3) User's tweet checking, please type 3\n"
                    "4) Leaving this app, please type quit\n:\t\n")

        if ask == "1":
            scrap_info()

        elif ask == "2":
            search_user_past_tweets()

        elif ask == "3":
            keywords_search()

        elif ask == "quit":
            quit()

        else:
            print("Sorry I don't understand !")

# Only run if it is called as main.py but not module
if __name__ == "__main__":
    main()


