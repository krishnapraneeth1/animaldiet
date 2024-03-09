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
# import customtkinter as ctk



#connecting to the database
pdsdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
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
        self.root.geometry("1100x750")
        self.root.config(bg="white")
    
        #frame for gif
        self.gif_frame = Frame(self.root, bg="white")
        self.gif_frame.place(x=300, y=300, width=500, height=450)

        #gif
        self.gif = GIF(self.gif_frame, 'gifs\dog_cat.gif')
        self.gif.config(highlightthickness=0, bd=0, relief="ridge")
        self.gif.pack()

        #remove frame border
        self.gif_frame.config(highlightbackground="white", highlightcolor="white", highlightthickness=0)





#starter code
if __name__ == "__main__":
    root = Tk()
    app = PawfectPortions(root)
    root.mainloop()