from tkinter import *

from PIL import Image, ImageTk
import os
import ast

# Creating a window
app = Tk()
app.title("Login Page")
app.geometry("1024x650")
app.configure(bg="white")

font1 = ("Times", 20, "bold")
font2 = ("Times", 15, "bold")
font3 = ("Times", 10, "bold")
font4 = ("Times", 10, "bold", "underline")

img = ImageTk.PhotoImage(Image.open("intro.jpg"))
Label(app, image=img).place(x=0, y=0)

#button = Button(app, text="")
#button.place(x=500, y=500)

frame = Frame(app, width= 250, height=190, bg="#deb685")  
frame.place(x=435, y=400)

heading = Label(frame,text="Login", font=font1,bg="#deb685")
heading.place(x=90, y=10)

#creating the labels and entry widgets for username and password
# for username
def on_click(event):
    username.delete(0, END)
def on_nonclick(event):
    if username.get() == "":
        username.insert(0, "Username")

username = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
username.place(x=30, y=50)
username.insert(0, "Username")
username.bind("<FocusIn>", on_click)
username.bind("<FocusOut>", on_nonclick)

Frame(frame, width=250, height=190, bg="white").place(x=435, y=400)
#for password
def on_click(event):
    password.delete(0, END)
def on_nonclick(event):
    if password.get() == "":
        password.insert(0, "Password")

password = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
password.place(x=30, y=90)
password.insert(0, "Password")
password.bind("<FocusIn>", on_click)
password.bind("<FocusOut>", on_nonclick)

Frame(frame, width=250, height=190, bg="white").place(x=495, y=490)



app.mainloop()


'''# login page
from tkinter import Tk, Label, Entry, Frame
from PIL import ImageTk, Image

def create_main_window():
    app = Tk()
    app.title("Login Page")
    app.geometry("1024x650")
    app.configure(bg="white")

    font1 = ("Times", 20, "bold")
    font2 = ("Times", 15, "bold")
    font3 = ("Times", 10, "bold")
    font4 = ("Times", 10, "bold", "underline")

    img = ImageTk.PhotoImage(Image.open("intro.jpg"))
    Label(app, image=img).place(x=0, y=0)

    frame = create_login_frame(app)
    
    app.mainloop()

def create_login_frame(parent):
    frame = Frame(parent, width=250, height=190, bg="#deb685")  
    frame.place(x=435, y=400)

    heading = Label(frame, text="Login", font=("Times", 20, "bold"), bg="#deb685")
    heading.place(x=90, y=10)

    username(frame, "Username", 30, 50)
    password(frame, "Password", 30, 90)

    return frame

def on_click(event):
    username.delete(0, 'end')

def on_nonclick(event, entry, username):
    if username.get() == "":
        username.insert(0, username)

    frame = Frame(frame, width=250, height=190, bg="white").place(x=435, y=400)
    username = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
    username.place(x=30, y=50)
    username.insert(0, "Username")
    username.bind("<FocusIn>", on_click)
    username.bind("<FocusOut>", on_nonclick)

def on_click(event, entry, password):
    entry.delete(0, 'end')

def on_nonclick(event):
    if password.get() == "":
        password.insert(0, password)
    frame = Frame(frame, width=250, height=190, bg="white").place(x=495, y=490)
    password = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
    password.place(x=30, y=90)
    password.insert(0, "Password")
    password.bind("<FocusIn>", on_click)
    password.bind("<FocusOut>", on_nonclick)








if __name__ == "__main__":
    create_main_window()'''

    
    
    