import tkinter as tk
from PIL import ImageTk, Image
import tweepy
import pandas as pd
import sqlite3
import json
import time
from tables import *
import requests

# constant variables
FONT = ("Agency FB", 18, "bold")
COLOR = "black"
ENTRY_WIDTH = 20


# Mission 1
class Twitter_Crawler_page1:
    def __init__(self, auth, api):
        # Login Menu Setting
        self.root = tk.Tk()
        self.root.title("Twitter Crawler")
        self.root.resizable(False,False)
        self.auth = auth
        self.api = api
        self.setinit()

    def setinit(self):
        """ Set Canvas """
        self.canvas = tk.Canvas(self.root, width=1230, height=650)
        self.canvas.pack(fill="both", expand=True)

        img = Image.open("p1.png")          # load image in python
        bg_image = ImageTk.PhotoImage(img)  # load image on tkinter


        self.profile_search = tk.Entry(self.canvas, width=ENTRY_WIDTH, justify='center')
        self.canvas.create_window(800, 60, window=self.profile_search)

        # post image on canvas
        self.canvas.create_image(0, 0, image = bg_image, anchor = "nw")

        serarch_img = tk.PhotoImage(file= "search.png")
        serarch_btn_img = tk.Button(self.root, image= serarch_img, command=self.search_click, highlightthickness=0, bd=0)
        serarch_btn = self.canvas.create_window(920, 40, anchor="nw", window=serarch_btn_img)
        self.canvas.pack()
        self.root.mainloop()

    def search_click(self):
        name = self.profile_search.get()
        self.scrap_info(name)

    
    def scrap_info(self, name):
        try:
            data_dict = {}   # Create dict to tranform into DataFrame
            lists = ["id", "name", "screen_name", "description", 
                    "followers_count", "friends_count", "created_at"]

            user = self.api.get_user(screen_name=name)     # get info from profile


            #import photo
            url = user.profile_image_url_https
            response = requests.get(url)
            with open("profile.png", "wb") as photo:
                photo.write(response.content)
            #self.upload_img()
            profile_img = Image.open("profile.png").resize((180, 180))
            self.profile_img = ImageTk.PhotoImage(profile_img)     

            self.canvas.create_image(140,140, anchor="nw", image=self.profile_img)    
            self.canvas.image = self.profile_img              
    
            str_ = json.dumps(user._json)             # Json to string
            json_ = json.loads(str_)                  # String to dict property

            for list in lists:
                data_dict[list] = json_[list]         

            conn = sqlite3.connect('project.db')      # connect to sqlite server and create database file
            cursor = conn.cursor()                    # to execute query in Python

            # COLLECT DATATIME -- FOR COMPARASION
            print(time.strftime("%a %d %b %Y %H:%M:%S"))

            # not change 
            cursor.execute(create_profile_table)
            conn.commit()   # update data 

            df = pd.DataFrame([data_dict])            # Dict to dataframe
            df.to_sql("profile", conn, if_exists='replace', index=False)    # DataFrame to SQLite
            print("Finish !!!")

        except sqlite3.IntegrityError as e:                # If duplicate, raise error to signal that you already have this data
            error_msg = tk.Toplevel(self.root)
            error_msg.title("Error")
            explanation = "You have already get this data!!!"
            tk.Label(error_msg,justify=tk.CENTER,text=explanation).pack(padx=50,pady=20)
            tk.Button(error_msg,text='OK',width=10,command=error_msg.destroy).pack(pady=8)

        except tweepy.errors.Forbidden as e:
            error_msg = tk.Toplevel(self.root)
            error_msg.title("Error")
            explanation = "User has been suspended !!!"
            tk.Label(error_msg,justify=tk.CENTER,text=explanation).pack(padx=50,pady=20)
            tk.Button(error_msg,text='OK',width=10,command=error_msg.destroy).pack(pady=8)

        except tweepy.errors.NotFound:
            error_msg = tk.Toplevel(self.root)
            error_msg.title("Error")
            explanation = "User not found !!!"
            tk.Label(error_msg,justify=tk.CENTER,text=explanation).pack(padx=50,pady=20)
            tk.Button(error_msg,text='OK',width=10,command=error_msg.destroy).pack(pady=8)




    

