#import python ,tkinter, mysql and other libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import re


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
    password VARCHAR(100) NOT NULL
)
"""

#executing the query
cursor = pdsdb.cursor()
cursor.execute(create_user_table)




#pds class
class PDS:
    def __init__(self, root):
        self.app = root
        self.app.title("PDS")
        self.app.geometry("1024x650")
        
        #display 
        img = Image.open("main1.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.app,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        
        
        self.app.after(2000,self.login_page)


        
    #first login page
    def login_page(self):
        #clear the window
        for i in self.app.winfo_children():
            i.destroy()
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
                self.new_username.insert(0, "Username/Email")
        
        self.new_username=Entry(self.l_frame,width=25,fg="black",bg="white",font=('Helvetica',12))
        self.new_username.place(x=49,y=65,height=28)
        self.new_username.insert(0,"Username/Email")
        self.new_username.bind("<FocusIn>", on_click)
        self.new_username.bind("<FocusOut>", on_nonclick)
        
        #for password entry 
        def on_click(event):
                self.new_password.delete(0, 'end')
                self.new_password.config(show="*")
        def on_nonclick(event):
            if self.new_password.get() == "":
               self.new_password.insert(0, "Password")
               self.new_password.config(show="")

        self.new_password =Entry(self.l_frame,width=25,fg="black",bg="white",font=("Helvetica", 12))
        self.new_password.place(x=50,y=107,height=28)
        self.new_password.insert(0,"Password")
        self.new_password.bind("<FocusIn>", on_click)
        self.new_password.bind("<FocusOut>", on_nonclick)
        
        
        
        
        #for forget password
        self.forget_password=Button(self.l_frame,text="Forget Password?",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.f_password)
        self.forget_password.place(x=100,y=150)
        
        #buttons
        #login button in the login page(first screen)
        self.login_page1=Button(self.l_frame,text="Login",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.login)
        self.login_page1.place(x=150,y=200)
        
        # for not a member text
        self.login_page1=Label(self.l_frame,text="Not a Member?",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.login_page1.place(x=120,y=240)
        
        #for sign up button in login page(first screen)
        self.login_page1=Button(self.l_frame,text="Sign Up",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.sign_up)
        self.login_page1.place(x=143,y=270)
        
        
    #signup_page_data(second screen) or create account page
    def signup_data(self):
        first_name = self.s_firstname.get()
        last_name = self.s_lastname.get()
        email = self.s_username.get()
        mobile = self.s_phone.get()
        password = self.s_password.get()
        confirm_password = self.s_c_password.get()
        
        
        #validations
        if first_name and not(first_name.isspace()) and last_name and not(last_name.isspace()) and email and not(email.isspace()) and mobile and not(mobile.isspace()) and password and not(password.isspace()) and confirm_password and not(confirm_password.isspace()):
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showerror("Error", "Invalid Email")
                return
            if not re.match(r"[0-9]{10}", mobile):
                messagebox.showerror("Error", "Invalid Mobile")
                return

            if password == confirm_password:
                try:
                    cursor = pdsdb.cursor()
                    cursor.execute("INSERT INTO user_info (first_name, last_name, email, mobile, password) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, email, mobile, password))
                    pdsdb.commit()
                    messagebox.showinfo("Success", "User created successfully")
                    self.login_page()
                except Error as e:
                    messagebox.showerror("Error", e)
            else:
                messagebox.showerror("Error", "Password and Confirm Password do not match")
        else:
            messagebox.showerror("Error", "All fields are required")
    
    #login page validation
    
    def login(self):
        username = self.new_username.get()
        password = self.new_password.get()
        
        if username and password:
            try:
                cursor = pdsdb.cursor()
                cursor.execute("SELECT * FROM user_info WHERE email=%s AND password=%s", (username, password))
                user = cursor.fetchone()
                if user:
                    messagebox.showinfo("Success", "Welcome "+username)
                else:
                    messagebox.showerror("Error", "Invalid Username/Email or Password")
            except Error as e:
                messagebox.showerror("Error", e)
        else:
            messagebox.showerror("Error", "All fields are required")
            
#forget password

    def f_password(self):
        for i in self.app.winfo_children():
            i.destroy()
       
        self.app.title("Forget Password")
        self.app.geometry("1024x650")
        #display image 
        img = Image.open("mainblur.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.app,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        
        self.up_frame=Frame(self.app,width=350,height=360,bg="white")
        self.up_frame.place(x=367,y=180)
        self.heading=Label(self.up_frame,text="Forget Password",font=("Helvetica",15,"bold"),bg="white",fg="black")
        self.heading.place(x=100,y=10)
        
        self.email_label=Label(self.up_frame,text="Email/Username",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.email_label.place(x=130,y=80)  
        
        self.email_entry=Entry(self.up_frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.email_entry.place(x=70,y=110)
        
        self.newpassword_label=Label(self.up_frame,text="New Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.newpassword_label.place(x=130,y=140)
        
        self.newpassword_entry=Entry(self.up_frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.newpassword_entry.place(x=70,y=170)
        
        self.confirm_newpassword_label=Label(self.up_frame,text="Confirm New Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.confirm_newpassword_label.place(x=110,y=200)   
        
        self.confirm_newpassword_entry=Entry(self.up_frame,width=25,fg="black",bg="white",font='Helvetica 12')
        self.confirm_newpassword_entry.place(x=70,y=230)
       
        #update password button
        self.update=Button(self.up_frame,text="Update",font=("Helvetica",10,"bold"),bg="white",fg="black",command=self.updatenew_password)
        self.update.place(x=160,y=270)
        
        #back to login page
        self.backtologin_page=Button(self.up_frame,text="Back to Login",font=("Helvetica",10,"bold"),bg="white",fg="black",command=self.login_page)
        self.backtologin_page.place(x=140,y=310)
       

# Assuming that pdsdb is your database connection object

        
    def updatenew_password(self):
        email = self.email_entry.get()
        cursor = pdsdb.cursor()
        try:
            cursor.execute("SELECT * from user_info WHERE email=%s", (email,))
            user = cursor.fetchone()
        except Error as e:
            messagebox.showerror("Error", e)
        if user:
            new_password = self.newpassword_entry.get()
            confirm_new_password = self.confirm_newpassword_entry.get()
            if email and new_password and confirm_new_password:
                if new_password == confirm_new_password:
                    try:
                        cursor = pdsdb.cursor()
                        cursor.execute("UPDATE user_info SET password=%s WHERE email=%s", (new_password, email))
                        pdsdb.commit()
                        messagebox.showinfo("Success", "Password updated successfully")
                        self.login_page()
                    except Error as e:
                        messagebox.showerror("Error", e)
                else:
                    messagebox.showerror("Error", "Password and Confirm Password do not match")
            else:
                messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showerror("Error", "Invalid Email")
    #sign up page or creat account page
    def sign_up(self):
        self.app.title("Sign Up Page")
        self.app.geometry("1024x650")
        #display image
        #clearing the window
        self.frame=Frame(self.app,width=1050,height=650,bg="white")
        self.frame.place(x=0,y=0)
        
       
        #inserintg signup image
        img = Image.open("mainblur.jpg")
        img=ImageTk.PhotoImage(img)
        self.label=Label(self.frame,image=img)
        self.label.image=img
        self.label.place(x=0,y=0)
        self.frame1=Frame(self.app,width=700,height=450,bg="white")
        self.frame1.place(x=180,y=90)
        
       
        #creat account label
        self.heading=Label(self.frame1,text="Create Account",font=("Helvetica",20,"bold"),bg="white",fg="black")
        self.heading.place(x=280,y=15)
        
        #for User inforamtion label
        self.user_info=Label(self.frame1,text="User Information",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.user_info.place(x=44,y=80)
        
        #for first name label and entry
        self.s_firstname=Label(self.frame1,text="First Name",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_firstname.place(x=44,y=120)
        self.s_firstname=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_firstname.place(x=120,y=120)
        
        #for last name label and entry
        self.s_lastname=Label(self.frame1,text="Last Name",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_lastname.place(x=370,y=120)
        self.s_lastname=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_lastname.place(x=460,y=120)
        
        #for email label and entry
        self.s_username=Label(self.frame1,text="Username/Email",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_username.place(x=44,y=160)
        self.s_username=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_username.place(x=155,y=160)
        
        #for phone number label and entry
        self.s_phone=Label(self.frame1,text="Mobile No.",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_phone.place(x=44,y=200)
        self.s_phone=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_phone.place(x=120,y=200)
        
        #for password label and entry  
        self.s_password=Label(self.frame1,text="Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_password.place(x=44,y=240)
        self.s_password=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_password.place(x=120,y=240)
        
        #for confirm password label and entry 
        self.s_c_password=Label(self.frame1,text="Confirm Password",font=("Helvetica",10,"bold"),bg="white",fg="black")
        self.s_c_password.place(x=334,y=240)
        self.s_c_password=Entry(self.frame1,width=25,fg="black",bg="white",font='Helvetica 12')
        self.s_c_password.place(x=460,y=240)
       
        
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
        
        # singup button in create account page
        self.signup=Button(self.frame1,text="Sign Up",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.signup_data)
        self.signup.place(x=315,y=300)
        
        #for already a member text
        self.login_page2=Label(self.frame1,text="Already a Member?",font=("Helvetica",12,"bold"),bg="white",fg="black")
        self.login_page2.place(x=288,y=350)
        
        #for login button in create account page
        self.login_page3=Button(self.frame1,text="Login",font=("Helvetica",12,"bold"),bg="white",fg="black",command=self.login_page)
        self.login_page3.place(x=330,y=380)
 
   



if __name__ == "__main__":
    root = Tk()
    app = PDS(root)
    #app.new_password()
    root.mainloop()