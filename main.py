from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import ast


class PetDieterSystem:
    #constructor method
    def __init__(self,app):
        #creating a window
        self.app = app
        self.app.title("Login Page")
        self.app.geometry("1024x650")
        self.app.configure(bg="white")
        self.login_page()
        
        
   
    def login_page(self):
        #display image
        img = Image.open("intro.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.app,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        
        
        #login frame
        self.frame=Frame(self.app,width=250,height=210,bg="#deb685")
        self.frame.place(x=435,y=380)
        self.heading=Label(self.frame,text="Login",font=("Times",20,"bold"),bg="#deb685",fg="black")
        self.heading.place(x=90,y=0)
        
        # for username entry
        def on_click(event):
            username.delete(0, 'end')
        def on_nonclick(event):
            if username.get() == "":
                username.insert(0, "Username")
        
        username=Entry(self.frame,width=25,fg="black",bg="#deb685",font='Times 12')
        username.place(x=30,y=37)
        username.insert(0,"Username")
        username.bind("<FocusIn>", on_click)
        username.bind("<FocusOut>", on_nonclick)
        
        #for password entry 
        def on_click(event):
            password.delete(0, 'end')
        def on_nonclick(event):
            if password.get() == "":
               password.insert(0, "Username")
        password =Entry(self.frame,width=25,fg="black",bg="#deb685",font='Times 12')
        password.place(x=30,y=67)
        password.insert(0,"Password")
        password.bind("<FocusIn>", on_click)
        password.bind("<FocusOut>", on_nonclick)
        
        #for forget password
        self.forget_password=Button(self.frame,text="Forget Password?",font=("Times",10,"bold"),bg="#deb685",fg="black")
        self.forget_password.place(x=78,y=100)
        
        #buttons
        self.login_page=Button(self.frame,text="Login",font=("Times",10,"bold"),bg="#deb685",fg="black")
        self.login_page.place(x=108,y=133)
        # for not a member text
        self.login_page=Label(self.frame,text="Not a Member?",font=("Times",10,"bold"),bg="#deb685",fg="black")
        self.login_page.place(x=30,y=175)
        #for sign up button
        self.login_page=Button(self.frame,text="Sign Up",font=("Times",10,"bold"),bg="#deb685",fg="black",command=self.sign_up)
        self.login_page.place(x=120,y=170)
        
        
        
        #for sign up frame
    def sign_up(self):

        for i in self.app.winfo_children():
            i.destroy()
        #signup frame
        self.app.title("Sign Up Page")
        self.app.geometry("1024x650")
        #display image
        #clearing the window
        self.frame=Frame(self.app,width=250,height=210,bg="red")
        self.frame.place(x=100,y=100)
        
        self.heading=tk.Label(self.frame,text="Create Account",font=("Times",20,"bold"),bg="white",fg="black")
        self.heading.place(x=90,y=90)

    
#starter code
#creating an object of the class
if __name__ == "__main__":
    app=Tk()
    project=PetDieterSystem(app)
    app.mainloop()

#checking git push
