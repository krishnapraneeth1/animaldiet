#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
# import re
import tkinter as tk
# from GIF import GIF
# from RAG import RAG


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
        # self.rag = RAG()
        
        
        #self.welcomeScreen()
        self.loginScreen()
    
    #login screen
    def loginScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #create a frame for the login screen
        self.login_frame = Frame(self.root, bg="white")
        self.login_frame.place(x=0, y=0, width=1200, height=750)
        # adding Logindogpage1 image
        self.bg = Image.open("images/Logindogpage1.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.login_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #adding Welcome text on the top
        self.welcome_label = Label(self.login_frame, text="Welcome.", font=("calibri", 70, "bold"), bg="black", fg="WHITE")
        self.welcome_label.place(x=100, y=70)
        
        #adding login text on the top
        self.login_label = Label(self.login_frame, text="Login", font=("calibri", 20, "bold"), bg="black", fg="WHITE")
        self.login_label.place(x=850, y=200)
        
        #adding username label
        self.username_label = Label(self.login_frame, text="_____________________", font=("calibri", 18, "bold"), bg="black", fg="WHITE") 
        self.username_label.place(x=760, y=270)
        #adding password label
        self.password_label = Label(self.login_frame, text="_____________________", font=("calibri", 18, "bold"), bg="black", fg="WHITE")
        self.password_label.place(x=760, y=340)
        
        #adding password entryc
        self.password_entry = Entry(self.login_frame,font=("calibri", 18), bg="black", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.password_entry.place(x=765, y=325)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind('<FocusIn>', self.removepasswordtext)
        self.password_entry.bind('<FocusOut>', self.removepasswordtext)
    
        #adding username entry
        self.username_entry = Entry(self.login_frame,font=("calibri", 18), bg="black", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.username_entry.place(x=765, y=260)
        self.username_entry.insert(0, "Email")
        #self.username_entry.bind("<Key>", self.removeusernametext)
        self.username_entry.bind('<FocusIn>', self.removeusernametext)
        self.username_entry.bind('<FocusOut>', self.removeusernametext)
        
        #adding login button
        self.login_button = Button(self.login_frame, text="Login", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black", command=self.welcomeScreen)
        self.login_button.place(x=850, y=400)
        #adding signup button
        self.signup_button = Button(self.login_frame, text="Sign Up", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black",command=self.signupScreen)
        self.signup_button.place(x=838, y=440)
        #adding forgot password button
        self.forgot_password_button = Button(self.login_frame, text="Forgot Password?", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black")
        self.forgot_password_button.place(x=783, y=480)
    
    
    #creating entry lable inside the username entry
    def removeusernametext(self, event):
        if self.username_entry.get() == "Email":
            self.username_entry.delete(0, "end")
            self.username_entry.config(fg="white")
        elif self.username_entry.get() == "":
            self.username_entry.insert(0, "Email")
            self.username_entry.config(fg="white") 
    def removepasswordtext(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="white")
            self.password_entry.config(show="*")
        elif self.password_entry.get() == "":
            self.password_entry.insert(0, "Password")
            self.password_entry.config(show="")
            self.password_entry.config(fg="white") 

    #creating signup screen
    def signupScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #create a frame for the signup screen
        self.signup_frame = Frame(self.root, bg="white")
        self.signup_frame.place(x=0, y=0, width=1200, height=750)
        # adding Logindogpage1 image
        self.bg = Image.open("images\signtupcat.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.signup_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.signup_label = Label(self.signup_frame, text="Register Your Account Here", font=("calibri", 40, "bold"), bg="#080808", fg="WHITE")
        self.signup_label.place(x=300, y=50)
        
        #adding first name label
        self.first_name_label = Label(self.signup_frame, text="First Name", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.first_name_label.place(x=40, y=200)
        #addling line under the first name label
        self.first_name_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.first_name_label.place(x=158, y=206)
        #adding first name entry
        self.first_name_entry = Entry(self.signup_frame,font=("calibri", 15), bg="#080808", width=28, bd=0,fg="white", relief="ridge",insertbackground="white")
        self.first_name_entry.place(x=160, y=206)
        #adding last name label 
        self.last_name_label = Label(self.signup_frame, text="Last Name", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.last_name_label.place(x=450, y=206)
        #addling line under the last name label
        self.last_name_label = Label(self.signup_frame, text="____________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.last_name_label.place(x=565, y=205)
        #adding last name entry
        self.last_name_entry = Entry(self.signup_frame,font=("calibri",15), bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.last_name_entry.place(x=570, y=206)
        #adding email label
        self.email_label = Label(self.signup_frame, text="Email", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.email_label.place(x=50, y=275)
        #addling line under the email label
        self.email_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.email_label.place(x=158, y=280)
        #adding email entry
        self.email_entry = Entry(self.signup_frame,font=("calibri", 15), width=28, bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.email_entry.place(x=160, y=280)
        #adding mobile label
        self.mobile_label = Label(self.signup_frame, text="Mobile", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.mobile_label.place(x=50, y=350)
        #addling line under the mobile label
        self.mobile_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.mobile_label.place(x=160, y=350)
        #adding mobile entry
        self.mobile_entry = Entry(self.signup_frame,font=("calibri", 15), bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.mobile_entry.place(x=160, y=350)
        #adding password label
        self.password_label = Label(self.signup_frame, text="Password", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.password_label.place(x=50, y=425)
        #addling line under the password label
        self.password_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.password_label.place(x=160, y=425)
        #adding password entry
        self.password_entry = Entry(self.signup_frame,font=("calibri", 15), width= 28, bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.password_entry.place(x=160, y=425)
        #adding confirm password label
        self.confirm_password_label = Label(self.signup_frame, text="Confirm Password", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.confirm_password_label.place(x=50, y=500)
        #addling line under the confirm password label
        self.confirm_password_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.confirm_password_label.place(x=250, y=495)
        #adding confirm password entry
        self.confirm_password_entry = Entry(self.signup_frame,font=("calibri", 15), width=28, bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white")
        self.confirm_password_entry.place(x=252, y=495)
        #adding signup button
        self.signup_button = Button(self.signup_frame, text="Sign Up", font=("calibri",18,"bold"), bg="#080808", fg="white", bd=0, cursor="hand2",activebackground="#080808")
        self.signup_button.place(x=485, y=590)
        #adding login button
        self.login_button = Button(self.signup_frame, text="Back to Login", font=("calibri",18,"bold"), bg="#080808", fg="white", bd=0, cursor="hand2",activebackground="#080808",command=self.loginScreen)
        self.login_button.place(x=460, y=650)
        

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
        self.bottom_frame.place(x=0, y=690, width=1200, height=80)
        #add shadow to the bottom frame
        self.bottom_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=0)
        
        #home button    
        self.home_button = Button(self.bottom_frame, text="Home", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.home_button.place(x=400, y=6)
        
        #dogs button
        self.dogs_button = Button(self.bottom_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        #command to dogs screen
        self.dogs_button.config(command=self.selectDogBreed)
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
        #commad=self.selectDogBreed
        self.dogs_button.config(command=self.selectDogBreed)    
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
        # self.ask_button = Button(self.rest_frame, text="Ask", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2",command=self.genetaeResponse)
        self.ask_button = Button(self.rest_frame, text="Ask", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.ask_button.place(x=550, y=250)
        
        
        #generate response
    # def genetaeResponse(self):
    #     #get the question from the entry box
    #     question = self.question_entry.get()
    #     #check if the question is empty
    #     if question == "":
    #         messagebox.showerror("Error", "Please enter a question")
    #         return
        
    #     response = self.rag.query(question)
        
    #     # print(response)
        
    #     #frame for the response
    #     self.response_frame = Frame(self.rest_frame, bg="black")
    #     self.response_frame.place(x=80, y=320, width=1000, height=300)
        
    #     #with borders
    #     self.response_frame.config(highlightbackground="white", highlightcolor="white", highlightthickness=1)
        
    #     #response label
    #     self.response_label = Label(self.response_frame, text=response, font=("calibri", 18), bg="black", fg="white")
    #     #if text is long, wrap it
    #     self.response_label.config(wraplength=950)
    #     self.response_label.place(x=10, y=10)
        
        
    #dogs screen
    def selectDogBreed(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
            
        #display selectbreed image full screen
        self.bg = Image.open("images/selectbreed.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
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
        
        #dogs button white
        self.dogs_button.config(bg="white", fg="#242323")
        
        
        #cats button
        self.cats_button = Button(self.buttons_frame, text="Cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        
        #Pet AI
        self.pet_ai_button = Button(self.buttons_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.pet_ai_button.config(command=self.petAiScreen)
        self.pet_ai_button.place(x=760, y=6)
        
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
        
        #select dog breed label bg #272727
        self.select_dog_breed_label = Label(self.root, text="Select Dog Breed", font=("calibri", 30, ), bg="#272727", fg="white")
        self.select_dog_breed_label.place(x=250, y=120)
        
        #dog breeds buttons as text
        #labrador button
        self.labrador_button = Button(self.root, text="Labrador", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.labrador_button.place(x=320, y=250)
        
        #german shepherd button
        self.german_shepherd_button = Button(self.root, text="German Shepherd", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.german_shepherd_button.place(x=280, y=320)
        
        
        #golden retriever button
        self.golden_retriever_button = Button(self.root, text="Golden Retriever", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.golden_retriever_button.place(x=290, y=390)
        
        #french bulldog button
        self.french_bulldog_button = Button(self.root, text="French Bulldog", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.french_bulldog_button.place(x=300, y=460)
        
        #siberian husky button
        self.siberian_husky_button = Button(self.root, text="Siberian Husky", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.siberian_husky_button.place(x=300, y=530)
        
        #config command for the buttons
        # self.labrador_button.config(command=self.dogScreen("Labrador"))
        # self.german_shepherd_button.config(command=self.dogScreen("German Shepherd"))
        # self.golden_retriever_button.config(command=self.dogScreen("Golden Retriever"))
        # self.french_bulldog_button.config(command=self.dogScreen("French Bulldog"))
        # self.siberian_husky_button.config(command=self.dogScreen("Siberian Husky"))
        
    #dog screen
    def dogScreen(self, breed):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #display dog breed image full screen
        self.bg = Image.open(f"images/{breed}.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root, bg="#242323")
        self.buttons_frame.place(x=0, y=0, width=1200, height=60)
        
        #home button
        self.home_button = Button(self.buttons_frame, text="Home", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.home_button.config(command=self.welcomeScreen)
        self.home_button.place(x=400, y=6)
        
        #dogs button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)
        
        #dogs button white
        self.dogs_button.config(bg="white", fg="#242323")
        
        #cats button
        self.cats_button = Button(self.buttons_frame, text="Cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        
        #Pet AI
        self.pet_ai_button = Button(self.buttons_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.pet_ai_button.config(command=self.petAiScreen)
        self.pet_ai_button.place(x=760, y=6)
        
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
        
        #display breed name label
        self.breed_label = Label(self.root, text=breed, font=("calibri", 30, "bold"), bg="#272727", fg="white")
        self.breed_label.place(x=500, y=120)
        
        
        
        

        
        
    
        

        
        
    
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        





#starter code
if __name__ == "__main__":
    root = Tk()
    app = PawfectPortions(root)
    root.mainloop()