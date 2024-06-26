import tkinter
#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import re
import tkinter as tk
from tkinter import ttk
import webbrowser
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
    email VARCHAR(100)  NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    mobile VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
    )
"""

#pettable
create_pet_table = """
CREATE TABLE IF NOT EXISTS pet_info (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    pet_type VARCHAR(100) NOT NULL DEFAULT 'dog',
    pet_name VARCHAR(100) NOT NULL,
    pet_breed VARCHAR(100) NOT NULL,
    pet_gender VARCHAR(100) NOT NULL,
    pet_color VARCHAR(100) NOT NULL,
    pet_age INT NOT NULL,
    image_path VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES user_info(user_id))
"""



#executing the query
cursor = pdsdb.cursor()
cursor.execute(create_user_table)
cursor.execute(create_pet_table)


#class Pawfect Portions as pp
class PawfectPortions:
    #initializing the class
    def __init__(self, root):
        self.root = root
        self.root.title("Pawfect Portions")
        self.root.geometry("1200x750")
        self.root.config(bg="white")
        self.rag = RAG()

        
        
        
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
        
        self.show_pass_var = tk.IntVar()
        self.password_visible = False
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
        self.username_label = Label(self.login_frame, text="__________________________", font=("calibri", 18, "bold"), bg="black", fg="WHITE") 
        self.username_label.place(x=760, y=270)
        #adding password label
        self.password_label = Label(self.login_frame, text="__________________________", font=("calibri", 18, "bold"), bg="black", fg="WHITE")
        self.password_label.place(x=760, y=340)
        
        #adding password entry
        self.password_entry = Entry(self.login_frame,font=("calibri", 18), bg="black", width=28, bd=0,fg="white", relief="ridge",insertbackground="white")
        self.password_entry.place(x=765, y=325)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind('<FocusIn>', self.removepasswordtext)
        self.password_entry.bind('<FocusOut>', self.removepasswordtext)
    
        #adding username entry
        self.username_entry = Entry(self.login_frame,font=("calibri", 18), bg="black", width= 28, bd=0,fg="white", relief="ridge",insertbackground="white")
        self.username_entry.place(x=765, y=260)
        self.username_entry.insert(0, "Email")
        #self.username_entry.bind("<Key>", self.removeusernametext)
        self.username_entry.bind('<FocusIn>', self.removeusernametext)
        self.username_entry.bind('<FocusOut>', self.removeusernametext)
        
        #adding show password icon
        show_icon_image = Image.open("images/show.png")
        show_icon_resized = show_icon_image.resize((30, 30), Image.Resampling.LANCZOS)  
        self.show_icon = ImageTk.PhotoImage(show_icon_resized)

        # Open and resize the hide icon
        hide_icon_image = Image.open("images/hide.png")
        hide_icon_resized = hide_icon_image.resize((30, 30), Image.Resampling.LANCZOS)  
        self.hide_icon = ImageTk.PhotoImage(hide_icon_resized)


        # Create a button to toggle password visibility
        self.toggle_button = tk.Button(self.login_frame, image=self.show_icon, command=self.toggle_password_visibility, borderwidth=0,highlightthickness=0, bg="black", activebackground="black")
        self.toggle_button.place(x=1050, y=330)
        
        
        #adding login button
        self.login_button = Button(self.login_frame, text="Login", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black",activeforeground="grey", command=self.login_validation)
        self.login_button.place(x=800, y=400)
        #adding signup button
        self.signup_button = Button(self.login_frame, text="Sign Up", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black",activeforeground="grey",command=self.signupScreen)
        self.signup_button.place(x=950, y=400)
        #adding forgot password button
        self.login_forgot_password_button = Button(self.login_frame, text="Forgot Password?", font=("calibri",10,"bold"), bg="black", fg="light blue", bd=0, cursor="hand2",activebackground="black",activeforeground="grey")
        self.login_forgot_password_button.place(x=960, y=380)
        self.login_forgot_password_button.config(command=self.forgotPassword)
#method for show and hide password icon
    def toggle_password_visibility(self):
        if self.password_visible:
            # Hide the password and update the button icon
            self.password_entry.config(show="*")
            self.toggle_button.config(image=self.show_icon)
            self.password_visible = False
        else:
            # Show the password and update the button icon
            self.password_entry.config(show="")
            self.toggle_button.config(image=self.hide_icon)
            self.password_visible = True
    
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
        self.password_entry = Entry(self.signup_frame,font=("calibri", 15), width= 28, bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white",show="*")
        self.password_entry.place(x=160, y=425)
        
         # Create a button to toggle password visibility
        self.toggle_button = tk.Button(self.signup_frame, image=self.show_icon, command=self.toggle_password_visibility, borderwidth=0,highlightthickness=0, bg="#080808", activebackground="black")
        self.toggle_button.place(x=425, y=420)
        
        #adding confirm password label
        self.confirm_password_label = Label(self.signup_frame, text="Confirm Password", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.confirm_password_label.place(x=50, y=500)
        #addling line under the confirm password label
        self.confirm_password_label = Label(self.signup_frame, text="_______________________", font=("calibri", 18, "bold"), bg="#080808", fg="WHITE")
        self.confirm_password_label.place(x=250, y=495)
        #adding confirm password entry
        self.confirm_password_entry = Entry(self.signup_frame,font=("calibri", 15), width=28, bg="#080808", bd=0,fg="white", relief="ridge",insertbackground="white",show="*")
        self.confirm_password_entry.place(x=252, y=495)
        #adding signup button
        self.signup_button = Button(self.signup_frame, text="Sign Up", font=("calibri",18,"bold"), bg="#080808", fg="white", bd=0, cursor="hand2",activebackground="#080808",activeforeground="grey")
        self.signup_button.place(x=485, y=590)
        self.signup_button.config(command=self.signup_data)
        #adding login button
        self.login_button = Button(self.signup_frame, text="Back to Login", font=("calibri",18,"bold"), bg="#080808", fg="white", bd=0, cursor="hand2",activebackground="#080808",activeforeground="grey",command=self.loginScreen)
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
        

        #bottom frame for buttons
        self.bottom_frame = Frame(self.root, bg="#242323")
        self.bottom_frame.place(x=0, y=690, width=1200, height=80)
        #add shadow to the bottom frame
        self.bottom_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=0)
        
        #add logo image as a button side to home button
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.bottom_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.bottom_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
        
        # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.bottom_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        #self.petprofile_button.config(command=self.dogProfileScreen)

  
        
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
        self.cats_button.config(command=self.selectCatBreed)
        
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
        self.facebook_button.config(command=self.selectfacebook)
        
        
        #place instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        self.instagram_button = Button(self.bottom_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        
        #twitter  icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        self.twitter_button = Button(self.bottom_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
    
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()
        
        
        #creating the social media methods
    def selectfacebook(self):
        webbrowser.open_new("https://www.facebook.com/pawfect.portions/")  

    def selectinstagram(self):
        webbrowser.open_new("https://www.instagram.com/pawfect._portions/")

    def selecttwitter(self):
        webbrowser.open_new("https://twitter.com/PawfectPortions")
    
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
        self.cats_button.config(command=self.selectCatBreed)
        
        #Pet AI
        self.pet_ai_button = Button(self.buttons_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.pet_ai_button.place(x=760, y=6)
        
        #highlight the pet ai button
        self.pet_ai_button.config(bg="white", fg="#242323")
        
        #add logo image as a button
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
         
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        
        
    
        #facebook icon as a button
        self.facebook_icon = Image.open("social/facebook.png")
        self.facebook_icon = self.facebook_icon.resize((25, 25), Image.LANCZOS)
        self.facebook_icon = ImageTk.PhotoImage(self.facebook_icon)
        
        self.facebook_button = Button(self.buttons_frame, image=self.facebook_icon, bg="#242323", bd=0, cursor="hand2")
        self.facebook_button.place(x=1000, y=13)
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        
        
    
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
        self.ask_button = Button(self.rest_frame, text="Ask", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2",command=self.generateResponse)
        # self.ask_button = Button(self.rest_frame, text="Ask", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.ask_button.place(x=550, y=250)
        
        
        #generate response
    def generateResponse(self):
        #get the question from the entry box
        question = self.question_entry.get()
        #check if the question is empty
        if question == "":
            messagebox.showerror("Error", "Please enter a question")
            return
        
        response = self.rag.query(question)
        
        # print(response)
        
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
        
        
        # Bind the petprofile_button to show the dropdown menu on left click
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu with a different design
        self.dropdown_menu = Menu(self.root, tearoff=0, bg="#242323", fg="white", bd=0, font=("calibri", 20, "bold"))
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self.catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)

       
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.config(bg='black', fg='white')  # Change background and foreground color
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.dropdown_menu.grab_release()

        
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
        self.cats_button.config(command=self.selectCatBreed)
        
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
    
        #select dog breed label bg #272727
        self.select_dog_breed_label = Label(self.root, text="Select Dog Breed", font=("calibri", 30, ), bg="#272727", fg="white")
        self.select_dog_breed_label.place(x=250, y=120)
        
        #dog breeds buttons as text
        #labrador button
        self.labrador_button = Button(self.root, text="Labrador", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.labrador_button.place(x=320, y=250)
        self.labrador_button.config(command=self.labradorScreen)
        
        #german shepherd button
        self.german_shepherd_button = Button(self.root, text="German Shepherd", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.german_shepherd_button.place(x=280, y=320)
        self.german_shepherd_button.config(command=self.germanScreen)
        
        
        #golden retriever button
        self.golden_retriever_button = Button(self.root, text="Golden Retriever", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.golden_retriever_button.place(x=290, y=390)
        self.golden_retriever_button.config(command=self.golden_retrever)
        
        #french bulldog button
        self.french_bulldog_button = Button(self.root, text="French Bulldog", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.french_bulldog_button.place(x=300, y=460)
        self.french_bulldog_button.config(command=self.frenchBulldogScreen)
        
        #siberian husky button
        self.siberian_husky_button = Button(self.root, text="Siberian Husky", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.siberian_husky_button.place(x=300, y=530)
        self.siberian_husky_button.config(command=self.siberian_husky)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

        #adding details of the breed under the top frame
        
        # adding a new frame for french bulldog
    def frenchBulldogScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #display selectbreed image full screen
        self.bg = Image.open("images/French Bulldog.jpg")
        self.bg = self.bg.resize((1300, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        #adding lable for the breed
        self.breed_label = Label(self.root, text="French Bulldog.", font=("calibri", 50,"bold"),bg="#eef4f4" ,fg="black")
        self.breed_label.place(x=40, y=100)
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#eef4f4", fg="black", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root , bg="#242323")
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.loginScreen)
        
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    
    def siberian_husky(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display selectbreed image full screen
        self.bg = Image.open("images/samplehusky.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#706e6f", fg="white", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#edeef2", fg="Black", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        
        #adding lable for the breed
        self.breed_label = Label(self.root, text="Husky.", font=("calibri", 50,"bold"), bg="#737172", fg="black")
        self.breed_label.place(x=20, y=60)
        
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root , bg="#242323")
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    
    def golden_retrever(self):
    #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display selectbreed image full screen
        self.bg = Image.open("images/golden.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#706e6f", fg="white", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#edeef2", fg="Black", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        
        #adding lable for the breed
        self.breed_label = Label(self.root, text="Golden Retrever.", font=("calibri", 50,"bold"), bg="#f9c847", fg="black")
        self.breed_label.place(x=20, y=60)
        
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root , bg="#242323")
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
        
            # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    def view_Profile(self):
        self.petprofile_button.config(command=self.view_Profile)

    def Dogpetprofile(self):
         self.petprofile_button.config(command=self.dogProfileScreen)
     
    def Catpetprofile(self):
        self.petprofile_button.config(command=self.catProfileScreen)

    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    # adding a new frame for labrador
    def labradorScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display selectbreed image full screen
        self.bg = Image.open("images/whitelab.jpg")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#edeef2", fg="Black", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        
        #adding lable for the breed
        self.breed_label = Label(self.root, text="Labrador.", font=("calibri", 60,"bold"), bg="#f8f8fa", fg="black")
        self.breed_label.place(x=50, y=120)
        
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root , bg="#242323")
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        self.profile_button.config(command=self.profileScreen)
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)

        # Dog="Labrador"
        # dog_details=self.rag.getDogDetails(Dog)
        
        
        #ask question about the labrador label
        self.labrador_label = Label(self.root, text="Ask Anything about the Labrardor.", font=("calibri", 20,"bold"), bg="#f8f8fa", fg="black")
        self.labrador_label.place(x=650, y=300)
        
        #Entry box for the question
        self.question_entry = Entry(self.root, font=("calibri", 18), bg="white", fg="black")
        self.question_entry.place(x=650, y=350, width=400, height=40)
        
        #ask button
        self.ask_button = Button(self.root, text="Ask", font=("calibri", 18, "bold"), bg="#f8f8fa", fg="black", bd=0, cursor="hand2", command=self.askLabrador)
        self.ask_button.place(x=1050, y=350)
        
    def askLabrador(self):
        dog="Labrador"
        question=self.question_entry.get()
        
        #get the answer from the database
        answer=self.rag.getAnswer(dog, question)
        
        #a frame to display the answer
        self.answer_frame = Frame(self.root)
        self.answer_frame.place(x=550, y=400, width=600, height=200)

        #display the answer
        self.answer_label = Label(self.answer_frame, text=answer, font=("calibri", 18),fg="black")
        self.answer_label.config(wraplength=450)
        self.answer_label.place(x=0, y=0)

        
        #clear the entry box
        self.question_entry.delete(0, END)
        
        
        

    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    
        
    def germanScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #display selectbreed image full screen
        self.bg = Image.open("images/german1.png")
        self.bg = self.bg.resize((1200, 750), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the dog breeds right bottom corner
        self.back_button = Button(self.root, text="Back", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.selectDogBreed)
        
        #adding lable for the breed
        self.breed_label = Label(self.root, text="German Shepherd.", font=("calibri", 40,"bold"),bg="#242323" ,fg="white")
        self.breed_label.place(x=40, y=100)
        
        
        #buttons frame on top
        self.buttons_frame = Frame(self.root , bg="#242323")
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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()


        #Cat Screen
    def selectCatBreed(self):
        #for clearing the previous window
        for i in self.root.winfo_children():
            i.destroy()
        #display cat breed image
        self.bg=Image.open("images/catbreed.JPEG")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)

        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

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
        self.facebook_button.config(command=self.selectfacebook)
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        

        #select Cat breed label bg #272727
        self.select_cat_breed_label = Label(self.root, text="Select Cat Breed", font=("calibri", 30, ), bg="#272727", fg="white")
        self.select_cat_breed_label.place(x=250, y=120)
        
        #Cat breeds buttons as text
        #Bengal cat button
        self.bengal_cat_button = Button(self.root, text="Bengal Cat", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.bengal_cat_button.config(command=self.selectBengalCat)
        self.bengal_cat_button.place(x=320, y=250)
        
        #Abyssinian button
        self.abyssinian_button = Button(self.root, text="Abyssinian", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.abyssinian_button.config(command=self.selectAbyss)
        self.abyssinian_button.place(x=320, y=320)
        
        
        #Rag doll button
        self.rag_doll_button = Button(self.root, text="Rag Doll", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.rag_doll_button.config(command=self.selectRagDoll)
        self.rag_doll_button.place(x=330, y=390)
        
        #Maine coon button
        self.maine_coon_button = Button(self.root, text="Maine Coon", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.maine_coon_button.config(command=self.selectMaineCoon)
        self.maine_coon_button.place(x=310, y=460)
        
        #British shorthair button
        self.British_shorthair_button = Button(self.root, text="British Shorthair", font=("calibri", 18, "bold"), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.British_shorthair_button.config(command=self.selectBrithishShorthair)
        self.British_shorthair_button.place(x=300, y=530)
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

    
    

    # Bengal Cat Screen
    def selectBengalCat(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display the Bengal Cat Image in full screen
        self.bg = Image.open("images/bengalcat.jpg")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

        # Back button
        self.back_button = Button(self.root, text="BACK", font=("calibri", 20), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.back_button.config(command=self.selectCatBreed)
        self.back_button.place(x=1050, y=680)

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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        #display bengal cat breed label bg #272727
        self.select_bengal_cat_label = Label(self.root, text="Bengal Cat", font=("calibri", 40, ), bg="black", fg="white")
        self.select_bengal_cat_label.place(x=150, y=120)
        
        # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

        
        # Abyssinian Cat Screen
    def selectAbyss(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display the Rag Doll Image in full screen
        self.bg = Image.open("images/Abyss.jpg")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

        # Back button
        self.back_button = Button(self.root, text="BACK", font=("calibri", 20), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.back_button.config(command=self.selectCatBreed)
        self.back_button.place(x=1050, y=680)

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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        

        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)



        #display Abyssinian breed label bg #272727
        self.select_Abyss_label = Label(self.root, text="Abyssinian", font=("calibri", 40, ), bg="black", fg="white")
        self.select_Abyss_label.place(x=100, y=120)
        
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

        
         # Rag Doll Screen
    def selectRagDoll(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display the Rag Doll Image in full screen
        self.bg = Image.open("images/ragdoll.jpg")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

        # Back button
        self.back_button = Button(self.root, text="BACK", font=("calibri", 20), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.back_button.config(command=self.selectCatBreed)
        self.back_button.place(x=1050, y=680)

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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)  
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        #display RagDoll breed label bg #272727
        self.select_RagDoll_label = Label(self.root, text="RagDoll", font=("calibri", 40, ), bg="black", fg="white")
        self.select_RagDoll_label.place(x=150, y=120)
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()
        
         # Maine Coon Screen
    def selectMaineCoon(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display the Rag Doll Image in full screen
        self.bg = Image.open("images/mainecoon.jpg")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

        # Back button
        self.back_button = Button(self.root, text="BACK", font=("calibri", 20), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.back_button.config(command=self.selectCatBreed)
        self.back_button.place(x=1050, y=680)

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
        self.facebook_button.config(command=self.selectfacebook)
        
        #instagram icon as a button
        self.instagram_icon = Image.open("social/insta.png")
        self.instagram_icon = self.instagram_icon.resize((25, 25), Image.LANCZOS)
        self.instagram_icon = ImageTk.PhotoImage(self.instagram_icon)
        
        self.instagram_button = Button(self.buttons_frame, image=self.instagram_icon, bg="#242323", bd=0, cursor="hand2")
        self.instagram_button.place(x=1050, y=15)
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        #display RagDoll breed label bg #272727
        self.select_maine_label = Label(self.root, text="Maine Coon", font=("calibri", 40, ), bg="black", fg="white")
        self.select_maine_label.place(x=150, y=120)
        
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()

       
          # Brithish Shorthair Screen
    def selectBrithishShorthair(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #display the Rag Doll Image in full screen
        self.bg = Image.open("images/Brithishshorthair.jpg")
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

        #Dogs Button
        self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.dogs_button.config(command=self.selectDogBreed)
        self.dogs_button.place(x=520, y=6)

        #cats button
        self.cats_button = Button(self.buttons_frame, text="cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        self.cats_button.place(x=640, y=6)
        #Cats button white
        self.cats_button.config(bg="White", fg="#242323")

        # Back button
        self.back_button = Button(self.root, text="BACK", font=("calibri", 20), bg="#272727", fg="white", bd=0, cursor="hand2")
        self.back_button.config(command=self.selectCatBreed)
        self.back_button.place(x=1050, y=680)

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
        self.instagram_button.config(command=self.selectinstagram)
        
        #twitter icon as a button
        self.twitter_icon = Image.open("social/twitter.png")
        self.twitter_icon = self.twitter_icon.resize((25, 25), Image.LANCZOS)
        self.twitter_icon = ImageTk.PhotoImage(self.twitter_icon)
        
        self.twitter_button = Button(self.buttons_frame, image=self.twitter_icon, bg="#242323", bd=0, cursor="hand2")
        self.twitter_button.place(x=1100, y=15)
        self.twitter_button.config(command=self.selecttwitter)
        
        #add logo image as a button 
        self.logo = Image.open("images/logout.jpg")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_button = Button(self.buttons_frame, image=self.logo, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.logo_button.place(x=20, y=10)
        self.logo_button.config(command=self.loginScreen)
        
        #add profile image as a button
        self.profile = Image.open("images/profile.png")
        self.profile = self.profile.resize((40, 40), Image.LANCZOS)
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_button = Button(self.buttons_frame, image=self.profile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.profile_button.place(x=90, y=10)
        
        #display Brithish Shorthair breed label bg #272727
        self.select_brithish_label = Label(self.root, text="Brithish Shorthair", font=("calibri", 40, ), bg="black", fg="white")
        self.select_brithish_label.place(x=150, y=120)
        
         # add Petprofile image as a button
        self.petprofile = Image.open("images/Petprofile.jpg")
        self.petprofile = self.petprofile.resize((60, 60), Image.LANCZOS)
        self.petprofile = ImageTk.PhotoImage(self.petprofile)
        self.petprofile_button = Button(self.buttons_frame, image=self.petprofile, bg="#242323", activebackground="#242323",bd=0, cursor="hand2")
        self.petprofile_button.place(x=145, y=0)
        
        self.petprofile_button.bind("<Button-1>", self.show_dropdown_menu)

        # Create the dropdown menu
        self.dropdown_menu = Menu(self.root, tearoff=0)
        self.dropdown_menu.add_command(label="View My Pet", command=self.view_Profile)
        self.dropdown_menu.add_command(label="Register Cat", command=self. catProfileScreen)
        self.dropdown_menu.add_command(label="Register Dog", command=self.dogProfileScreen)
    #dropdown menu for the pet profile
    def show_dropdown_menu(self, event):
        """Show the dropdown menu near the button."""
        try:
            self.dropdown_menu.tk_popup(event.x_root, event.y_root)
        finally:
        
            self.dropdown_menu.grab_release()
        
        
        
        # #config command for the buttons
        # self.labrador_button.config(command=self.dogScreen("Labrador"))
        # self.german_shepherd_button.config(command=self.dogScreen("German Shepherd"))
        # self.golden_retriever_button.config(command=self.dogScreen("Golden Retriever"))
        # self.french_bulldog_button.config(command=self.dogScreen("French Bulldog"))
        # self.siberian_husky_button.config(command=self.dogScreen("Siberian Husky"))
        
    
    # adding signup page entry boxes data to the database
    def signup_data(self):
    #get the data from the entry boxes
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
         #check if the data is empty
        if first_name == "" or last_name == "" or email == "" or mobile == "" or password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required")
            return
        #email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid Email")
            return
        #mobile validation
        if not re.fullmatch(r"^[0-9]{10}$", mobile):
            messagebox.showerror("Error", "Invalid Mobile Number")
            return
        #password validation
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
            messagebox.showerror("Error", "Password must contain at least 8 characters, including letters and numbers")
            return
        #check if the password and confirm password are the same
        if password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password should be the same")
            return
        # inserting the data to the database
        cursor = pdsdb.cursor()
        insert_data = f"INSERT INTO user_info (email,first_name,last_name, mobile, password) VALUES ('{email}', '{first_name}', '{last_name}',  '{mobile}', '{password}')"
        cursor.execute(insert_data)
        pdsdb.commit()
        messagebox.showinfo("Success", "You have successfully registered")
        self.loginScreen()
        
    #login page validation with the database
    def login_validation(self):
        #get the data from the entry boxes
        email = self.username_entry.get()
        password = self.password_entry.get()
        
        # checking the email and password with the database
        cursor = pdsdb.cursor()
        select_data = f"SELECT * FROM user_info WHERE email = '{email}' AND password = '{password}'"
        cursor.execute(select_data)
        user = cursor.fetchone()

        if user:
            self.user_id=user[0]
            self.first_name=user[1]
            self.last_name=user[2]
            self.email=user[3]
            self.mobile=user[4]
            self.current_password=user[5]
            self.welcomeScreen()
        elif email == "admin" and password == "admin":
            self.adminScreen()
        else:
            messagebox.showerror("Error", "Invalid Email or Password")
            return
        
    #forgot password page
    def forgotPassword(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #crete a new frame for the forgot password page
        self.forgot_password_frame = Frame(self.root, bg="black")
        self.forgot_password_frame.place(x=0, y=0, width=1200, height=750)
        
        
        #forgot password label
        self.forgot_password_label = Label(self.root, text="Forgot Password", font=("calibri", 30), bg="black", fg="white")
        self.forgot_password_label.place(x=500, y=20)
        
        #email label
        self.email_label = Label(self.root, text="Email:", font=("calibri", 20), bg="black", fg="white")
        self.email_label.place(x=400, y=100)
        
        #email entry
        self.email_entry = Entry(self.root, font=("calibri", 20), bd=0)
        self.email_entry.place(x=500, y=100)
        
        #submit button
        self.forgot_password_submit_button = Button(self.root, text="Submit", font=("calibri", 18), bg="black", fg="white", bd=0, cursor="hand2")
        self.forgot_password_submit_button.place(x=600, y=150)
        self.forgot_password_submit_button.config(command=self.updatePassword)
        
        #back button
        self.back_button = Button(self.root, text="Back", font=("calibri", 18,"bold"), bg="black", fg="white", bd=0, cursor="hand2")
        self.back_button.place(x=600, y=400)
        self.back_button.config(command=self.loginScreen)
        

        
        
    #after submitting the email, check if the email is in the database and update the password
    def updatePassword(self):
        
        entered_email = self.email_entry.get()

    # Print the entered email address
        #print("Entered Email Address:", entered_email)
        
        self.entered_email = Label(self.root, text=entered_email, font=("calibri", 20), bg="black", fg="white")
        self.entered_email.place(x=500, y=100)
        
        self.forgot_password_submit_button.destroy()

        # Remove the email entry box
        self.email_entry.destroy()
        
        #check if the email is in the database
        cursor = pdsdb.cursor()
        select_data = f"SELECT * FROM user_info WHERE email = '{entered_email}'"
        cursor.execute(select_data)
        user = cursor.fetchone()
            
        if user:
            #update the password
            self.new_password = Label(self.root, text="Enter new Password:", font=("calibri", 20), bg="black", fg="white")
            self.new_password.place(x=250, y=200)
            
            self.new_password_entry = Entry(self.root, font=("calibri", 20), bd=0)
            self.new_password_entry.place(x=500, y=200)
            
            self.new_confirm_password_label = Label(self.root, text="Confirm Password:", font=("calibri", 20), bg="black", fg="white")
            self.new_confirm_password_label.place(x=250, y=250)
            
            self.new_confirm_password_entry = Entry(self.root, font=("calibri", 20), bd=0)
            self.new_confirm_password_entry.place(x=500, y=250)

            self.submit_button = Button(self.root, text="Upate Password", command=self.update_new_password, font=("calibri", 20), bg="black", fg="white",activebackground="black", bd=0, cursor="hand2")
            self.submit_button.place(x=550, y=300)
            
        else:
            messagebox.showerror("Error", "Email Not Found")
            self.loginScreen()

    def update_new_password(self):

            #password validation
            if len(self.new_password_entry.get()) < 8 or not re.search("[a-z]", self.new_password_entry.get()) or not re.search("[A-Z]", self.new_password_entry.get()) or not re.search("[0-9]", self.new_password_entry.get()):
                messagebox.showerror("Error", "Password must contain at least 8 characters, including letters and numbers")
                return
            #check if the password and confirm password are the same
            if self.new_password_entry.get() != self.new_confirm_password_entry.get():
                messagebox.showerror("Error", "Password and Confirm Password should be the same")
                return
            else:
                
                
                new_password = self.new_confirm_password_entry.get()
                email = self.email_entry.get()
                cursor = pdsdb.cursor()
                update_data = f"UPDATE user_info SET password = '{new_password}' WHERE email = '{email}'"
                cursor.execute(update_data)
                pdsdb.commit()
                messagebox.showinfo("Success", "Password Updated")
                self.loginScreen()
   
   
   
 
   
   
   
   
    #creating a profile page window and displaying the user details that are stored in the database for the signed in user
    def profileScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #creating a new frame for the profile page
        self.profile_frame = Frame(self.root, bg="black")
        self.profile_frame.place(x=0, y=0, width=1200, height=750)
        self.userprofile = Image.open("images/userprofilebg.jpg")
        self.userprofile = self.userprofile.resize((1200, 750), Image.LANCZOS)
        self.userprofile = ImageTk.PhotoImage(self.userprofile)
        self.userprofile_image = Label(self.profile_frame, image=self.userprofile).place(x=0, y=0, relwidth=1, relheight=1)
        
       
    
        #profile label
        self.profile_label = Label(self.profile_frame, text="My Profile", font=("calibri", 30), bg="#010204", fg="white")
        self.profile_label.place(x=550, y=20)
        
        #First Name label
        self.first_name_label = Label(self.profile_frame, text="First Name:", font=("calibri", 20), bg="#010204", fg="white")
        self.first_name_label.place(x=400, y=100)
        
        #Last Name label
        self.last_name_label = Label(self.profile_frame, text="Last Name:", font=("calibri", 20), bg="#010204", fg="white")
        self.last_name_label.place(x=400, y=150)
        
        #Email label
        self.email_label = Label(self.profile_frame, text="Email:", font=("calibri", 20), bg="#010204", fg="white")
        self.email_label.place(x=400, y=200)
        
        #Mobile label
        self.mobile_label = Label(self.profile_frame, text="Mobile:", font=("calibri", 20), bg="#010204", fg="white")
        self.mobile_label.place(x=400, y=250)

        #display data as label
        self.first_name_label = Label(self.profile_frame, text=self.first_name, font=("calibri", 20), bg="#010204", fg="white")
        self.first_name_label.place(x=600, y=100)

        self.last_name_label = Label(self.profile_frame, text=self.last_name, font=("calibri", 20), bg="#010204", fg="white")
        self.last_name_label.place(x=600, y=150)

        self.email_label = Label(self.profile_frame, text=self.email, font=("calibri", 20), bg="#010204", fg="white")
        self.email_label.place(x=600, y=200)

        self.mobile_label = Label(self.profile_frame, text=self.mobile, font=("calibri", 20), bg="#010204", fg="white")
        self.mobile_label.place(x=600, y=250)

        
        #back button
        self.back_button = Button(self.profile_frame, text="Back", font=("calibri", 18), bg="#010204", fg="white", bd=0, cursor="hand2",activebackground="#010204", activeforeground="white")
        self.back_button.place(x=580, y=310)
        self.back_button.config(command=self.welcomeScreen)

        #update password button
        self.update_password_button = Button(self.profile_frame, text="Update Password", font=("calibri", 18), bg="#010204", fg="white", bd=0, cursor="hand2",activebackground="#010204", activeforeground="white")
        self.update_password_button.place(x=750, y=310)
        self.update_password_button.config(command=self.validatePassword)
        
       #view my pet profile
        
    #updatePassword
    def validatePassword(self):
        #clear profile_frame
        for i in self.profile_frame.winfo_children():
            i.destroy()
        
        #Enter your current password
        self.current_password_label = Label(self.profile_frame, text="Enter Current Password:", font=("calibri", 20), bg="#010204", fg="white")
        self.current_password_label.place(x=400, y=100)

        self.current_password_entry = Entry(self.profile_frame, font=("calibri", 20), bg="#010204", fg="white", bd=0)
        self.current_password_entry.place(x=400, y=200)

        #validate the current password
        self.validate_password_button = Button(self.profile_frame, text="Validate Password", font=("calibri", 18), bg="#010204", fg="white", bd=0, cursor="hand2",activebackground="#010204", activeforeground="white")
        self.validate_password_button.place(x=400, y=300)
        self.validate_password_button.config(command=self.updatePassword)

    #update the password
    def updatePassword(self):
        #check if password is correct
        current_password = self.current_password_entry.get()

        if current_password!=self.current_password:

            #passwords donot match
            messagebox.showerror("Error", "Incorrect Password")
            return
        else:
            #New Password label
            self.new_password_label = Label(self.profile_frame, text="Enter New Password:", font=("calibri", 20), bg="#010204", fg="white")
            self.new_password_label.place(x=400, y=100)

            self.new_password_entry = Entry(self.profile_frame, font=("calibri", 20), bg="#010204", fg="white", bd=0)
            self.new_password_entry.place(x=400, y=200)

            #Confirm Password label
            self.confirm_password_label = Label(self.profile_frame, text="Confirm Password:", font=("calibri", 20), bg="#010204", fg="white")
            self.confirm_password_label.place(x=400, y=250)

            self.confirm_password_entry = Entry(self.profile_frame, font=("calibri", 20), bg="#010204", fg="white", bd=0)
            self.confirm_password_entry.place(x=400, y=350)

            #update password button
            self.update_password_button = Button(self.profile_frame, text="Update Password", font=("calibri", 18), bg="#010204", fg="white", bd=0, cursor="hand2",activebackground="#010204", activeforeground="white")
            self.update_password_button.place(x=400, y=450)

            self.update_password_button.config(command=self.updatePassword_db)

            #cancel button
            self.cancel_button = Button(self.profile_frame, text="Cancel", font=("calibri", 18), bg="#010204", fg="white", bd=0, cursor="hand2",activebackground="#010204", activeforeground="white")
            self.cancel_button.place(x=600, y=450)

            self.cancel_button.config(command=self.profileScreen)

    #updatePassword_db
    def updatePassword_db(self):
        #get the new password
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        #password validation
        if len(new_password) < 8 or not re.search("[a-z]", new_password) or not re.search("[A-Z]", new_password) or not re.search("[0-9]", new_password):
            messagebox.showerror("Error", "Password must contain at least 8 characters, including letters and numbers")
            return
        #check if the password and confirm password are the same
        if new_password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password should be the same")
            return
        else:
            #update the password
            cursor = pdsdb.cursor()
            update_data = f"UPDATE user_info SET password = '{new_password}' WHERE email = '{self.email}'"
            cursor.execute(update_data)
            pdsdb.commit()
            messagebox.showinfo("Success", "Password Updated")
            self.loginScreen()




     
    #Dog pet profile page
    def dogProfileScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #creating a new frame for the pet profile page
        self.pet_profile_frame = Frame(self.root, bg="black")
        self.pet_profile_frame.place(x=0, y=0, width=1200, height=750)
        
        self.dogbg =Image.open("images/dogprofile.jpg")
        self.dogbg = self.dogbg.resize((1200, 750), Image.LANCZOS)
        self.dogbg = ImageTk.PhotoImage(self.dogbg)
        self.dogbg_image = Label(self.pet_profile_frame, image=self.dogbg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the home page
        self.back_button = Button(self.pet_profile_frame, text="Back", font=("calibri", 18, "bold"), bg="#010101", fg="white", bd=0, cursor="hand2",activebackground="black", activeforeground="white")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.welcomeScreen)
        
        #pet profile label 
        self.pet_profile_label = Label(self.pet_profile_frame, text="Sign Up Your Dog Profile", font=("calibri", 40), bg="#010101", fg="white")
        self.pet_profile_label.place(x=430, y=30)
        
        #pet name label
        self.pet_name_label = Label(self.pet_profile_frame, text="Pet Name:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_name_label.place(x=470, y=150)
        
        #pet name label
        self.pet_name_label = Label(self.pet_profile_frame, text="_____________________", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_name_label.place(x=590, y=150)
        
        #pet name entry box
        self.pet_name_entry = Entry(self.pet_profile_frame, font=("calibri", 20),bg="#010101", bd=0,fg="white",relief="ridge",insertbackground="white")
        self.pet_name_entry.place(x=590, y=146)


        #pet breed dropdown menu below the pet name to select the breed German Shepherd, Labrador, French Bulldog, Golden Retriever, Siberian husky
        self.pet_breed_label = Label(self.pet_profile_frame, text="Pet Breed:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_breed_label.place(x=470, y=200)
        self.pet_breed = StringVar()
        self.pet_breed.set("Select Breed")
        self.pet_breed_dropdown = OptionMenu(self.pet_profile_frame, self.pet_breed, "German Shepherd", "Labrador", "Golden Retriever", "French Bulldog", "Siberian Husky")
        self.pet_breed_dropdown.config(bg="#010101", fg="white")
        self.pet_breed_dropdown.place(x=607, y=205)
        

        
        #pet gender label
        self.pet_gender_label = Label(self.pet_profile_frame, text="Gender:", font=("calibri", 20), bg="black", fg="white")
        self.pet_gender_label.place(x=470, y=250)  
        
        #radio buttons for pet gender male or female
        self.gender = StringVar(value=" ")
        self.male_radio = Radiobutton(self.pet_profile_frame,text="Male", variable=self.gender,value="Male", font=("calibri", 20), bg="#010101", fg="white", selectcolor="black")
        self.male_radio.place(x=583, y=247)
        
        self.female_radio = Radiobutton(self.pet_profile_frame,text="Female", variable=self.gender,value="Female",font=("calibri", 20), bg="#010101", fg="white", selectcolor="black")
        self.female_radio.place(x=700, y=247)
        
        #pet age label
        self.pet_age_label = Label(self.pet_profile_frame, text="Pet Age:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_age_label.place(x=470, y=300)

        #pet age in months and years
        self.months = StringVar()
        self.years = StringVar()

        #create dropdown menu for years
        self.years_label = Label(self.pet_profile_frame, text="Years:", font=("calibri", 20), bg="#010101", fg="white")
        self.years_label.place(x=590, y=300) 
        self.years_dropdown = OptionMenu(self.pet_profile_frame, self.years, *range(0, 15))
        self.years_dropdown.config(bg="#010101", fg="white")
        self.years_dropdown.place(x=663, y=303) 
        #create dropdown menu for months
        self.months_label = Label(self.pet_profile_frame, text="Months:", font=("calibri", 20), bg="#010101", fg="white")
        self.months_label.place(x=740, y=300)  
        self.months_dropdown = OptionMenu(self.pet_profile_frame, self.months, *range(0, 11))
        self.months_dropdown.config(bg="#010101", fg="white")
        self.months_dropdown.place(x=840, y=303)  
        
        #pet color label
        self.pet_color_label = Label(self.pet_profile_frame, text="Pet Color:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_color_label.place(x=470, y=350)  
        
        #pet color label
        self.pet_color_label = Label(self.pet_profile_frame, text="_____________________", font=("calibri", 20), bg="white", fg="white")
        self.pet_color_label.place(x=590, y=350)
        
        #pet color entry box
        self.pet_color_entry = Entry(self.pet_profile_frame, font=("calibri", 20), bg="#010101", fg="white", bd=0, relief="ridge", insertbackground="white")
        self.pet_color_entry.place(x=590, y=350)
        
        
        #submit button
        self.pet_profile_submit_button = Button(self.pet_profile_frame, text="Submit", font=("calibri", 20), bg="#010101", fg="white", bd=0, cursor="hand2",activebackground="black", activeforeground="white")
        self.pet_profile_submit_button.place(x=650, y=485)
        self.pet_profile_submit_button.config(command=self.dogpetProfileData)
        
    #adding the dog pet profile data to the database

    #dogpetProfileData
    def dogpetProfileData(self):
        #take data
        pet_name = self.pet_name_entry.get()
        pet_breed = self.pet_breed.get()
        pet_gender = self.gender.get()
        years = self.years.get()
        months = self.months.get()
        pet_age = int(years)*12 + int(months)
        pet_color = self.pet_color_entry.get()
  
        #check if the data is empty
        if pet_name == "" or pet_breed == "Select Breed" or pet_gender == " " or pet_age == " " or pet_color == "":
            messagebox.showerror("Error", "All fields are required")
            return
        #insert the data to the database
        cursor = pdsdb.cursor()
        insert_data = f"INSERT INTO pet_info (user_id, pet_type, pet_name,pet_breed, pet_gender, pet_color, pet_age) VALUES ({self.user_id}, 'Dog', '{pet_name}', '{pet_breed}', '{pet_gender}', '{pet_color}', '{pet_age}')"
        cursor.execute(insert_data)
        pdsdb.commit()
        messagebox.showinfo("Success", "Pet Profile Created")
        self.welcomeScreen()


    
    def catProfileScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
        
        #creating a new frame for the pet profile page
        self.pet_profile_frame = Frame(self.root, bg="black")
        self.pet_profile_frame.place(x=0, y=0, width=1200, height=750)
        
        self.dogbg =Image.open("images/catprofile.jpg")
        self.dogbg = self.dogbg.resize((1200, 750), Image.LANCZOS)
        self.dogbg = ImageTk.PhotoImage(self.dogbg)
        self.dogbg_image = Label(self.pet_profile_frame, image=self.dogbg).place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #create a back button to go back to the home page
        self.back_button = Button(self.pet_profile_frame, text="Back", font=("calibri", 18, "bold"), bg="#010101", fg="white", bd=0, cursor="hand2",activebackground="Black", activeforeground="white")
        self.back_button.place(x=1000, y=650)
        self.back_button.config(command=self.welcomeScreen)
        
        #pet profile label 
        self.pet_profile_label = Label(self.pet_profile_frame, text="Sign Up Your Cat Profile", font=("calibri", 40), bg="#010101", fg="white")
        self.pet_profile_label.place(x=430, y=30)
        
        #pet name label
        self.pet_name_label = Label(self.pet_profile_frame, text="Pet Name:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_name_label.place(x=470, y=150)
        
        #pet name label
        self.pet_name_label = Label(self.pet_profile_frame, text="_____________________", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_name_label.place(x=590, y=150)
        
        #pet name entry box
        self.pet_name_entry = Entry(self.pet_profile_frame, font=("calibri", 20),bg="#010101", bd=0,fg="white",relief="ridge",insertbackground="white")
        self.pet_name_entry.place(x=590, y=146)


        #pet breed dropdown menu below the pet name to select the breed German Shepherd, Labrador, French Bulldog, Golden Retriever, Siberian husky
        self.pet_breed_label = Label(self.pet_profile_frame, text="Pet Breed:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_breed_label.place(x=470, y=200)
        self.pet_breed = StringVar()
        self.pet_breed.set("Select Breed")
        self.pet_breed_dropdown = OptionMenu(self.pet_profile_frame, self.pet_breed, "Bengal Cat", "Abyssinian", "Rag Doll", "Maine coon", "British shorthair")
        self.pet_breed_dropdown.config(bg="#010101", fg="white")
        self.pet_breed_dropdown.place(x=607, y=205)
        

        
        #pet gender label
        self.pet_gender_label = Label(self.pet_profile_frame, text="Gender:", font=("calibri", 20), bg="black", fg="white")
        self.pet_gender_label.place(x=470, y=250)  
        
        #radio buttons for pet gender male or female
        self.gender = StringVar(value=" ")
        self.male_radio = Radiobutton(self.pet_profile_frame,text="Male", variable=self.gender,value="Male", font=("calibri", 20), bg="#010101", fg="white", selectcolor="black")
        self.male_radio.place(x=583, y=247)
        
        self.female_radio = Radiobutton(self.pet_profile_frame,text="Female", variable=self.gender,value="Female",font=("calibri", 20), bg="#010101", fg="white", selectcolor="black")
        self.female_radio.place(x=700, y=247)
        
        #pet age label
        self.pet_age_label = Label(self.pet_profile_frame, text="Pet Age:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_age_label.place(x=470, y=300)

        #pet age in months and years
        self.months = StringVar()
        self.years = StringVar()

        #create dropdown menu for years
        self.years_label = Label(self.pet_profile_frame, text="Years:", font=("calibri", 20), bg="#010101", fg="white")
        self.years_label.place(x=590, y=300) 
        self.years_dropdown = OptionMenu(self.pet_profile_frame, self.years, *range(0, 16))
        self.years_dropdown.config(bg="#010101", fg="white")
        self.years_dropdown.place(x=663, y=303) 
        #create dropdown menu for months
        self.months_label = Label(self.pet_profile_frame, text="Months:", font=("calibri", 20), bg="#010101", fg="white")
        self.months_label.place(x=740, y=300)  
        self.months_dropdown = OptionMenu(self.pet_profile_frame, self.months, *range(0, 11))
        self.months_dropdown.config(bg="#010101", fg="white")
        self.months_dropdown.place(x=840, y=303)  
        
        #pet color label
        self.pet_color_label = Label(self.pet_profile_frame, text="Pet Color:", font=("calibri", 20), bg="#010101", fg="white")
        self.pet_color_label.place(x=470, y=350)  
        
        #pet color label
        self.pet_color_label = Label(self.pet_profile_frame, text="_____________________", font=("calibri", 20), bg="white", fg="white")
        self.pet_color_label.place(x=590, y=350)
        
        #pet color entry box
        self.pet_color_entry = Entry(self.pet_profile_frame, font=("calibri", 20), bg="#010101", fg="white", bd=0, relief="ridge", insertbackground="white")
        self.pet_color_entry.place(x=590, y=350)
        
        
        #submit button
        self.pet_profile_submit_button = Button(self.pet_profile_frame, text="Submit", font=("calibri", 20), bg="#010101", fg="white", bd=0, cursor="hand2",activebackground="black", activeforeground="white")
        self.pet_profile_submit_button.place(x=650, y=485)
        #self.pet_profile_submit_button.config(command=self.catpetProfileData)
        
        
  


    #pet profile screen
    def view_Profile(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.pet_profile_frame= Frame(self.root,bg="black")
        self.pet_profile_frame.place(x=0,y=0,width=1200,height=750)
        
        self.pet_profile_image = Image.open("images/userprofilebg.jpg")
        self.pet_profile_image = self.pet_profile_image.resize((1200,750),Image.LANCZOS)
        self.pet_profile_photo = ImageTk.PhotoImage(self.pet_profile_image)
        self.pet_profile_frame_image = Label(self.pet_profile_frame,image=self.pet_profile_photo)
        self.pet_profile_frame_image.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        #title label My Pet Profile
        self.pet_profile_title = Label(self.pet_profile_frame,text="My Pet Profile",font=("calibri",30),bg="black",fg="white")
        self.pet_profile_title.place(x=500,y=20)

        #get data from pets table with user id
        cursor = pdsdb.cursor()
        select_data = f"SELECT * FROM pet_info WHERE user_id = {self.user_id}"
        cursor.execute(select_data)
        pets = cursor.fetchall()
        print(pets)

        # #iterate through the pets and display the data
        # for i, pet in enumerate(pets):
            

        
        #back button
        self.back_button = Button(self.pet_profile_frame,text="Back",font=("calibri",18),bg="black",fg="white",bd=0,cursor="hand2")
        self.back_button.place(x=600,y=400)
        self.back_button.config(command=self.welcomeScreen)

  
        
            
        
   
   
        
 
    
    
        
    
    #admin page
    def adminScreen(self):
        #clear the window
        for i in self.root.winfo_children():
            i.destroy()
            
        #creating a new frame for the admin page
        self.admin_frame = Frame(self.root, bg="black")
        self.admin_frame.place(x=0, y=0, width=1200, height=750)
        
        #admin label
        self.admin_label = Label(self.admin_frame, text="Admin Page", font=("calibri", 30), bg="black", fg="white")
        self.admin_label.place(x=500, y=20)
        
        #back button
        self.back_button = Button(self.admin_frame, text="Back", font=("calibri", 18), bg="black", fg="white", bd=0, cursor="hand2")
        self.back_button.place(x=600, y=400)
        self.back_button.config(command=self.loginScreen)
        
   
        

    
        
        
        
        
        # #buttons frame on top
        # self.buttons_frame = Frame(self.root, bg="#242323")
        # self.buttons_frame.place(x=0, y=0, width=1200, height=60)
        
        
        # #home button
        # self.home_button = Button(self.buttons_frame, text="Home", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        # self.home_button.config(command=self.welcomeScreen)
        # self.home_button.place(x=400, y=6)
        
        # #dogs button
        # self.dogs_button = Button(self.buttons_frame, text="Dogs", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        # self.dogs_button.config(command=self.selectDogBreed)
        # self.dogs_button.place(x=520, y=6)
        
        # #dogs button white
        # self.dogs_button.config(bg="white", fg="#242323")
        
        # #cats button
        # self.cats_button = Button(self.buttons_frame, text="Cats", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        # self.cats_button.place(x=640, y=6)
        
        # #Pet AI
        # self.pet_ai_button = Button(self.buttons_frame, text="Pet AI", font=("calibri", 18, "bold"), bg="#242323", fg="white", bd=0, cursor="hand2")
        # self.pet_ai_button.config(command=self.petAiScreen)
        # self.pet_ai_button.place(x=760, y=6)
        
        # #facebook icon as a button
        # self.facebook_icon = Image.open("social/facebook.png")  
        
        
        
      
       

        
        
    
        

        
        
    
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        





#starter code
if __name__ == "__main__":
    root = Tk()
    app = PawfectPortions(root)
    root.mainloop()