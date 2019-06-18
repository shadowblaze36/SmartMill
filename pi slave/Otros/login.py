# Developer: Norman A. Cubilla
# Program: Login
# Date: 19/12/2018
from Tkinter import *
from ttk import *
#from menu2 import *
import tkFont
import tkMessageBox
import os
import time
import datetime
import mysql.connector

v0=Tk()
v0.title("SECURITY DOOR LOGIN")
v0.geometry("650x450+400+100")
# ---- Vector -------

# Definition of functions

def login_process():
                    name1=user.get()
                    pass1=password.get()
                    if name1=='':
                                 tkMessageBox.showinfo("Save",message="Name is empty")
                    elif pass1=='':
                                   tkMessageBox.showinfo("Save",message="Password is empty")
                    elif name1=='' and pass1=='':
                                                 tkMessageBox.showinfo("Save",message="Name and Password are empty")
                    else:
                         conexion=mysql.connector.connect(
                                                          host="localhost",
                                                          user="root",
                                                          password="meduza1",
                                                          database="uth"
                                                         )
                                             
                         # Creation of Cursor
                         cursor=conexion.cursor()
                         sql=""" select * from users where name=("%s") and num_pass=("%s");"""%((name1),(pass1))
                         cursor.execute(sql)
                         if cursor.fetchall():
                                              os.system("sudo python /home/pi/menu2.py")
                         else:
                              text_error=tkFont.Font(family="Helvetica",size=8, weight="bold")
                              label_error=Label(v0,text="<<< PASSWORD OR USER INCORRECT >>>",font=text_error,foreground="red").place(x=310,y=250)
                       
def add():
          os.system("sudo python /home/pi/useradd.py")

def update():
             os.system("sudo python /home/pi/userupdate.py")

def lists():
            os.system("sudo python /home/pi/userslist2.py")

def delete():
             os.system("sudo python /home/pi/deleteuser.py")
        
image_logo=PhotoImage(file="image_login.png")
button_logo=Button(v0,image=image_logo).place(x=100,y=100,width=150,height=150)
# --- Labels ---------
textfont=tkFont.Font(family="Times New Roman",size=18)
textfont2=tkFont.Font(family="Times New Roman",size=14)
label1=Label(v0,text="UTH SECURITY DOOR",font=textfont).place(x=80,y=10)
image_uth=PhotoImage(file="logouth.gif")
button=Button(v0,image=image_uth).place(x=10,y=10)
# ----- Variables -----
user=StringVar()
password=StringVar()
# ---- Entries --------
label2=Label(v0,text="USER :",font=textfont2).place(x=300,y=130)
textbox1=Entry(v0,textvariable=user,width=15).place(x=370,y=130)
label3=Label(v0,text="PASS :",font=textfont2).place(x=300,y=170)
textbox2=Entry(v0,textvariable=password,width=15).place(x=370,y=170)
#---- Buttons ---------
button_login=Button(v0,text="LOGIN",command=login_process).place(x=390,y=210)

#----------------------------CRUD -----------------------------
image_add=PhotoImage(file="add.gif")
button_add=Button(v0,image=image_add,command=add).place(x=100,y=310)
image_edit=PhotoImage(file="edit.gif")
button_edit=Button(v0,image=image_edit,command=update).place(x=200,y=310)
image_query=PhotoImage(file="list.gif")
button_query=Button(v0,image=image_query,command=lists).place(x=300,y=310)
image_delete=PhotoImage(file="delete.gif")
button_delete=Button(v0,image=image_delete,command=delete).place(x=400,y=310)

v0.mainloop()
