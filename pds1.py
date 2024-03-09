#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import re
import tkinter as tk
from GIF import GIF
from RAG import RAG



#connecting to the database
pdsdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Croatia@24",
    database="pds"
)

#creating table user query userid,first_name,last_name,email,mobile,password
create_user_table = """
CREATE TABLE IF NOT EXISTS user_info (  
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    pet_name VARCHAR(100),
    pet_breed VARCHAR(100),
    petcolor VARCHAR(100)
    )
"""

#executing the query
cursor = pdsdb.cursor()
cursor.execute(create_user_table)


#class Pawfect Portions as pp
class PawfectPortions:
    #initializing the class
    def __init__(self, root):
        self.root = root
        self.root.title("Pawfect Portions")
        self.root.geometry("1200x750")
        self.root.config(bg="white")
        self.rag = RAG()
        
        
        self.welcomeScreen()
        
        
    #welcome screen
    def welcomeScreen(self):
        
        
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
                
        #dsiplay welcome image
        self.bg = Image.open("images/welcome.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #display title image on left middle
        self.title = Image.open("txtImages/title.png")
        self.title = self.title.resize((570, 200), Image.LANCZOS)
        self.title = ImageTk.PhotoImage(self.title)
        self.title_image = Label(self.root, image=self.title, bg="white")
        self.title_image.config(highlightthickness=0, bd=0, relief="ridge")
        self.title_image.place(x=20, y=140)
    
        # #frame for gif
        # self.gif_frame = Frame(self.root, bg="white")
        # self.gif_frame.place(x=300, y=300, width=500, height=450)

        # #gif
        # self.gif = GIF(self.gif_frame, 'gifs\dog_cat.gif')
        # self.gif.config(highlightthickness=0, bd=0, relief="ridge")
        # self.gif.pack()

        # #remove frame border
        # self.gif_frame.config(highlightbackground="white", highlightcolor="white", highlightthickness=0)


        #bottom frame for buttons
        self.bottom_frame = Frame(self.root, bg="#242323")
        self.bottom_frame.place(x=0, y=690, width=1200, height=60)
        #add shadow to the bottom frame
        self.bottom_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=0)
        
        #home button    
        self.home_button = Button(self.bottom_frame, text="Home", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.home_button.place(x=400, y=6)
        
        #dogs button
        self.dogs_button = Button(self.bottom_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.place(x=520, y=6)
        
        #cats button
        self.cats_button = Button(self.bottom_frame, text="Cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        
        #Pet AI
        self.pet_ai_button = Button(self.bottom_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        #command=self.petAiScreen
        self.pet_ai_button.config(command=self.petAiScreen)
        self.pet_ai_button.place(x=760, y=6)
        
        
        #place facebook icon as a button
        self.facebook_icon = Image.open("social/facebook.png")
        self.facebook_icon = self.facebook_icon.resize((25, 25), Image.LANCZOS)
        self.facebook_icon = ImageTk.PhotoImage(self.facebook_icon)
        self.facebook_button = Button(self.bottom_frame, image=self.facebook_icon, bg="#242323", bd=0, cursor="hand2")
        self.facebook_button.place(x=1000, y=13)
        
        
        #place instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        self.instagram_button = Button(self.bottom_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        
        
        #twitter  icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        self.twitter_button = Button(self.bottom_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        
    
    #petai screen
    def petAiScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root, bg="#242323")
        self.buttons_frame.place(x=0, y=0, width=1200, height=60)
        
        #home button
        self.home_button = Button(self.buttons_frame, text="Home", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.home_button.config(command=self.welcomeScreen)
        self.home_button.place(x=400, y=6)
        
        #dogs button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.place(x=520, y=6)
        
        #cats button
        self.cats_button = Button(self.buttons_frame, text="Cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        
        #Pet AI
        self.pet_ai_button = Button(self.buttons_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.pet_ai_button.place(x=760, y=6)
        
        #highlight the pet ai button
        self.pet_ai_button.config(bg="white", fg="#242323")
        
        #facebook icon as a button
        self.facebook_icon = Image.open("social/facebook.png")
        self.facebook_icon = self.facebook_icon.resize((25, 25), Image.LANCZOS)
        self.facebook_icon = ImageTk.PhotoImage(self.facebook_icon)
        
        self.facebook_button = Button(self.buttons_frame, image=self.facebook_icon, bg="#242323", bd=0, cursor="hand2")
        self.facebook_button.place(x=1000, y=13)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        
    
        #rest as frame for the rest of the screen with black background
        self.rest_frame = Frame(self.root, bg="black")
        self.rest_frame.place(x=0, y=60, width=1200, height=690)
        
        
        #i'm your pet ai label
        self.pet_ai_label = Label(self.rest_frame, text="I'm your Pet AI", font=("calibri", 30, "bold"), bg="black", fg="white")
        self.pet_ai_label.place(x=500, y=20)
        
        #you can ask me anything about your pet, ask a question label, or ask me to explain the behavior of your pet
        self.ask_label = Label(self.rest_frame, text="You can ask me anything about your pet, ask a question, or ask me to explain the behavior of your pet", font=("calibri", 18), bg="black", fg="white")
        self.ask_label.place(x=80, y=80)
         
        #Example: What are the best foods for my dog?
        self.example_label = Label(self.rest_frame, text="Example: What are the best foods for my dog?", font=("calibri", 18), bg="black", fg="white")
        self.example_label.place(x=400, y=120)
        
        
        #entry box for the question big and wide
        self.question_entry = Entry(self.rest_frame, font=("calibri", 18), bg="white", fg="black", relief="ridge")
        #center the text
        self.question_entry.config(justify="center")
        
        #rounded corners
        self.question_entry.config(highlightthickness=0, bd=0)
        self.question_entry.config(highlightbackground="black", highlightcolor="black")
        self.question_entry.place(x=80, y=180, width=1000, height=50)
        
        #ask button
        self.ask_button = Button(self.rest_frame, text="Ask", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2",command=self.genetaeResponse)
        self.ask_button.place(x=550, y=250)
        
        
        #generate response
    def genetaeResponse(self):
        #get the question from the entry box
        question = self.question_entry.get()
        #check if the question is empty
        if question == "":
            messagebox.showerror("Error", "Please enter a question")
            return
        
        response = self.rag.query(question)
        
        print(response)
        
        #frame for the response
        self.response_frame = Frame(self.rest_frame, bg="black")
        self.response_frame.place(x=80, y=320, width=1000, height=300)
        
        #with borders
        self.response_frame.config(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        
        #response label
        self.response_label = Label(self.response_frame, text=response, font=("calibri", 18), bg="black", fg="white")
        #if text is long, wrap it
        self.response_label.config(wraplength=950)
        self.response_label.place(x=10, y=10)
        
        
            
        
        
        
        
        
        
        
        
        
        
        





#starter code
if __name__ == "__main__":
    root = Tk()
    app = PawfectPortions(root)
    root.mainloop()