import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql
from PIL import Image, ImageTk
from tkmacosx import Button
#from tkinter import *
import os
import re

def show_login():
    create_account_frame.pack_forget()
    login_frame.pack(padx=30, pady=30)   

def show_create_account_screen():
    login_frame.pack_forget()
    create_account_frame.pack()
    update_background_image("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg")

#Function to create account
def create_account():
    c_username=create_username_entry.get()
    c_password=create_password_entry.get()

    if c_username == "" or c_password == "" :
        mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
    else:
        con = sql.connect(host="localhost", user="root", password="Croatia@24", database="login_details")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

            # Insert data into the table
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (c_username, c_password))

        
        con.commit()
        mb.showinfo(title="created account status",message="successful")
        con.close()

#Function for login
def login():
    e_username=login_username_entry.get()
    e_password=login_password_entry.get()

   

    if e_username == "" or e_password == "":
        mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
    else:
        con = sql.connect(host="localhost", user="root", password="Croatia@24", database="login_details")
        cursor=con.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (e_username, e_password))
        data = cursor.fetchone()

        if data:
             mb.showinfo(title="Login successful", message="Welcome, " + e_username)
        else:
            mb.showinfo(title = "Login Usuccessful",message="Username or Password are incorrect. If you are new user create a new account" )

def update_background_image(image_path):
    img = Image.open(image_path)
    resized_image = img.resize((1530, 800), Image.LANCZOS)
    image_tk = ImageTk.PhotoImage(resized_image)
    background_label.configure(image=image_tk)
    background_label.image = image_tk

   # if username == "" or password == "" :
     #  mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
    #else:
      #   mb.showinfo(title = "create an account",message="create a username and password for your account" )

#Main Window
root = tk.Tk()
root.title("Welcome to flipzon")
root.geometry("1540x800")
root.configure(bg="white")
root.attributes('-alpha', 0.9)
root.style = tk.ttk.Style()
root.style.theme_use("clam")

img = Image.open("C:/Users/prane/Downloads/_defd105c-4bb3-46e3-826a-562cc387d98e.jpeg")
resized_image = img.resize((1530, 800), Image.LANCZOS)
image_tk = ImageTk.PhotoImage(resized_image)
background_label = tk.Label(root, image=image_tk)
background_label.image = image_tk  # Keep a reference
background_label.place(x=0, y=0, relwidth=1, relheight=1)

'''img = ImageTk.PhotoImage(Image.open("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg"))
tk.Label(root, image=img).place(relheight=1, relwidth=1)'''




#Login frame
login_frame=tk.Frame(root, bg="grey")
#login_frame.place(x=0,y=0,relheight=1, relwidth=1)
#login_frame.attributes('-alpha', 0.9)
login_label = tk.Label(login_frame, text="provide your login details",bg="grey",font=("Calibri","20","bold"))
login_label.grid(row=0,column=0,columnspan=5,pady=10)
login_username_label= tk.Label(login_frame, text="username",bg="grey",fg="azure",font=("Calibri","15","bold"),pady=5)
login_username_entry= tk.Entry(login_frame)
login_password_label= tk.Label(login_frame, text="password",bg="grey",font=("Calibri","15","bold"))
login_password_entry= tk.Entry(login_frame)
login_button = Button(login_frame, text="Login",bg="#FFFF00",fg="black",command=login,highlightbackground="grey",borderless=1)
createacc_button= Button(login_frame, text="New User? Create Your account",bg="red",fg="black",command=show_create_account_screen,highlightbackground="grey",borderless=1)

login_username_label.grid(row=1,column=0)
login_username_entry.grid(row=1, column=1)
login_password_label.grid(row=2,column=0)
login_password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2,pady="10")
createacc_button.grid(row=4,column=0,columnspan=3)

#Create your account frame
create_account_frame=tk.Frame(root,bg="grey")
create_label = tk.Label(create_account_frame, text="create your account here",bg="grey",font=("Calibri","20","bold"))
create_label.grid(row=0,column=0,columnspan=5,pady=10)
create_username_label= tk.Label(create_account_frame, text="username",bg="grey",fg="azure",font=("Calibri","15","bold"),pady="5")
create_username_entry= tk.Entry(create_account_frame)
create_password_label= tk.Label(create_account_frame, text="password",bg="grey",font=("Calibri","15","bold"),pady="5")
create_password_entry= tk.Entry(create_account_frame)
create_button = Button(create_account_frame, text="Create",bg="blue",command=create_account,highlightbackground="grey")

create_username_label.grid(row=1,column=0)
create_username_entry.grid(row=1, column=1)
create_password_label.grid(row=2,column=0)
create_password_entry.grid(row=2,column=1)
create_button.grid(row=3,column=0,columnspan=2,pady="10")

show_login()

root.mainloop()
