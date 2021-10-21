import tkinter as tk
from PIL import ImageTk, Image
import tweepy

# constant variables
FONT = ("Agency FB", 18, "bold")
COLOR = "black"
ENTRY_WIDTH = 45
SCREEN_NAME = ""

class Twitter_Crawler_login_menu:
    def __init__(self):
        # Login Menu Setting
        self.root = tk.Tk()
        self.root.title("Twitter Crawler")
        self.root.resizable(False,False)
        self.setinit()


    def setinit(self):
        """ Set Canvas """
        self.canvas = tk.Canvas(self.root, width=1230, height=650)
        self.canvas.pack(fill="both", expand=True)
        img = Image.open("bg.png") # load image in python
        bg_image = ImageTk.PhotoImage(img) # load image on tkinter

        # post image on canvas
        self.canvas.create_image(0, 0, image = bg_image, anchor = "nw")

        """ Set Entry """
        self.new_entries = []
        locations = [(380, 278), (380, 328), (380, 378), (380, 428)]

        for location in locations:
            object = tk.Entry(self.canvas, width=ENTRY_WIDTH, justify='center')
            self.canvas.create_window(location[0], location[1], window=object)
            self.new_entries.append(object)

        self.canvas.pack()

        """ Set Labels """
        location = {"Consumer Key": (120, 278), "Consumer Secret": (120, 328), "Access Key": (120, 378), "Access Token Secret": (120, 428)}

        for key, value in location.items():
            self.canvas.create_text(value[0], value[1], text=key, fill=COLOR, font=FONT)

        self.canvas.pack()
    
        """ Set Buttons """
        start_img = tk.PhotoImage(file= "start_button.png")
        start_btn_img = tk.Button(self.root, image=start_img, command=self.start_click, highlightthickness=0, bd=0)

        """ Display Buttons """
        start_btn = self.canvas.create_window(180, 500, anchor="nw", window=start_btn_img)
        self.canvas.pack()
        self.root.mainloop()


    # Press the start button and go to next page 
    def start_click(self):
        self.consumer_key = self.new_entries[0].get()
        self.consumer_secret = self.new_entries[1].get()
        self.access_token = self.new_entries[2].get()
        self.access_token_secret = self.new_entries[3].get()
        self.auth_stage(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

    def auth_stage(self, consumer_key, consumer_secret, access_token, access_token_secret):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth)
            self.api.auth.get_authorization_url()
            
            successful_msg = tk.Toplevel(self.root)
            successful_msg.title("Success !!")
            explanation = "Login sucessful"
            tk.Label(successful_msg,justify=tk.CENTER,text=explanation).pack(padx=5,pady=2)
            tk.Button(successful_msg,text='OK',width=10,command=successful_msg.destroy).pack(pady=8)

        except tweepy.errors.TweepyException as e:
            error_msg = tk.Toplevel(self.root)
            error_msg.title("Error")
            explanation = "Could not authenticate you.\nPlease check your keys and fill-in correctly"
            tk.Label(error_msg,justify=tk.CENTER,text=explanation).pack(padx=50,pady=20)
            tk.Button(error_msg,text='OK',width=10,command=error_msg.destroy).pack(pady=8)


        