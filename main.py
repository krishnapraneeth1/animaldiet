from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import os
import ast
import mysql.connector
import re





class PetDieterSystem:
    #constructor method
    def __init__(self,app):
        #creating a window
        self.app = app
        self.app.title("Login Page")
        self.app.geometry("1024x650")
        self.app.configure(bg="white")
        
        img = Image.open("main1.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.app,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        
        '''self.login_page()'''
        self.app.after(1000, self.login_page)
        
# create account function

    '''def create_account(self):
        n_username = new_username.get()
        n_password = new_password.get()
        
        if n_username == "" or n_password == "":
            mb.showinfo("Empty", "Please fill the empty fields")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Croatia@24",database="petdietery")
            cursor.conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS (username,password) VALUES(%s,%s)",(n_username,n_password))'''
            
       
   
    def login_page(self):
        
        for i in self.app.winfo_children():
            i.destroy()
        #display image
        img = Image.open("mainblur.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.app,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        
        
        #login frame
        self.l_frame=Frame(self.app,width=350,height=360,bg="white")
        self.l_frame.place(x=367,y=180)
        self.heading=Label(self.l_frame,text="Login",font=("Helvetica",20,"bold"),bg="white",fg="black")
        self.heading.place(x=140,y=10)
        
        # for username entry
        def on_click(event):
            self.new_username.delete(0, 'end')
        def on_nonclick(event):
            if self.new_username.get() == "":
                self.new_username.insert(0, "Username")
        
        self.new_username=Entry(self.l_frame,width=25,fg="black",bg="white",font=('Helvetica',12,"bold"))
        self.new_username.place(x=49,y=65,height=28)
        self.new_username.insert(0,"Username")
        self.new_username.bind("<FocusIn>", on_click)
        self.new_username.bind("<FocusOut>", on_nonclick)
        
        #for password entry 
        def on_click(event):
            self.new_password.delete(0, 'end')
        def on_nonclick(event):
            if self.new_password.get() == "":
               self.new_password.insert(0, "Password")
        self.new_password =Entry(self.l_frame,width=25,fg="black",bg="white",font=("Helvetica", 12,"bold"))
        self.new_password.place(x=50,y=107,height=28)
        self.new_password.insert(0,"Password")
        self.new_password.bind("<FocusIn>", on_click)
        self.new_password.bind("<FocusOut>", on_nonclick)
        
        
        
        #for forget password
        self.forget_password=Button(self.l_frame,text="Forget Password?",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.f_password)
        self.forget_password.place(x=100,y=150)
        
        #buttons
        self.login_page1=Button(self.l_frame,text="Login",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.login)
        self.login_page1.place(x=150,y=200)
        # for not a member text
        self.login_page1=Label(self.l_frame,text="Not a Member?",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.login_page1.place(x=120,y=240)
        #for sign up button
        self.login_page1=Button(self.l_frame,text="Sign Up",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.sign_up)
        self.login_page1.place(x=143,y=270)
        
    #for login connection with db
    def user_details(self):
        n_username = self.new_username.get()
        n_password = self.new_password.get()
        
        if n_username == "" or n_password == "":
            mb.showinfo("Empty", "Please fill the empty fields")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Croatia@24",database="petdietery")
            cursor=conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS login_details (username VARCHAR(255), password VARCHAR(255),)")
            cursor.execute("INSERT INTO login_details (username, password) VALUES (%s, %s)", (self.username, self.password))
            
            conn.commit()
            mb.showinfo(title="created account status",message="successful")
            conn.close()
                
    def login(self):
            n_username = self.new_username.get()
            n_password = self.new_password.get()
        
            if n_username == "" or n_password == "":
                mb.showinfo("Empty", "Please fill the empty fields")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Croatia@24",database="petdietery")
                cursor=conn.cursor()
                
                cursor.execute("SELECT * FROM login_details WHERE username = %s AND password = %s", (n_username, n_password))
                data = cursor.fetchone()

                if data:
                    mb.showinfo(title="Login successful", message="Welcome, " + n_username)
                else:
                    mb.showinfo(title = "Login Usuccessful",message="Username or Password are incorrect. If you are new user create a new account" )

                         
        
        #for sign up frame
    def sign_up(self):

        for i in self.app.winfo_children():
            i.destroy()
        #signup frame
        self.app.title("Sign Up Page")
        self.app.geometry("1024x650")
        #display image
        #clearing the window
        self.frame=Frame(self.app,width=1050,height=650,bg="white")
        self.frame.place(x=0,y=0)
        
       
        #inserintg signup image
        img = Image.open("mainblur.jpg")
        '''img = img.resize((300, 300))'''
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.frame,image=img)
        self.label.image=img
        '''self.label.place(x=780,y=580)'''
        self.label.place(x=0,y=0)
        self.frame1=Frame(self.app,width=700,height=450,bg="white")
        self.frame1.place(x=180,y=90)
        
       
        #creat account label
        self.heading=tk.Label(self.frame1,text="Create Account",font=("Helvetica",20,"bold"),bg="white",fg="black")
        self.heading.place(x=280,y=15)
        
        #for User inforamtion label
        self.user_info=Label(self.frame1,text="User Information",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.user_info.place(x=44,y=80)
        
        #for first name label and entry
        self.username=Label(self.frame1,text="First Name",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=44,y=120)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=120)
        
        #for last name label and entry
        self.username=Label(self.frame1,text="Last Name",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=370,y=120)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=460,y=120)
        
        #for email label and entry
        self.username=Label(self.frame1,text="Email",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=44,y=160)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=160)
        
        #for phone number label and entry
        self.username=Label(self.frame1,text="Mobile No.",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=44,y=200)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=200)
        
        #for password label and entry  
        self.username=Label(self.frame1,text="Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=44,y=240)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=240)
        
        #for confirm password label and entry 
        self.username=Label(self.frame1,text="Confirm Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=334,y=240)
        self.username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=460,y=240)
        
        '''#for pet details label
        self.pet_details=Label(self.frame,text="Pet Details",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.pet_details.place(x=50,y=300)
        
        #for pet name label and entry
        self.username=Label(self.frame,text="Pet Name",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=50,y=340)
        self.username=Entry(self.frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=340)
        
        #for pet age label and entry
        self.username=Label(self.frame,text="Pet Age",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=50,y=380)
        self.username=Entry(self.frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=380)
        
        #for pet weight label and entry
        self.username=Label(self.frame,text="Pet Weight",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=50,y=420)
        self.username=Entry(self.frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=420)
        
        #for pet breed label and entry
        self.username=Label(self.frame,text="Pet Breed",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=50,y=460)
        self.username=Entry(self.frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.username.place(x=120,y=460)
        
        #for pet type label and entry
        self.username=Label(self.frame,text="Pet Type",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.username.place(x=50,y=507)
        #creating a drop down menu for pet type
        pet_type = ['Dog','Cat',"Bird","Fish"]
        self.seleted_pet_type = tk.StringVar()
        self.seleted_pet_type.set(pet_type[0])
        self.drop = tk.OptionMenu(self.frame, self.seleted_pet_type, *pet_type) #*pet_type unpacking the iterables(it allows you to pass the individual elements of an in a list)
        self.drop.place(x=120,y=500)'''
        
        # singup button
        self.signup=Button(self.frame1,text="Sign Up",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.user_details)
        self.signup.place(x=315,y=300)
        
        #for already a member text
        self.login_page2=Label(self.frame1,text="Already a Member?",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.login_page2.place(x=288,y=350)
        
        #for login button
        self.login_page3=Button(self.frame1,text="Login",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.login_page)
        self.login_page3.place(x=330,y=380)
 
 
 
      
#starter code
#creating an object of the class
if __name__ == "__main__":
    app=Tk()
    project=PetDieterSystem(app)
    #login()  
    app.mainloop()


