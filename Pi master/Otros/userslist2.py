# Developer: Cubillax
# date: 9/12/2018
# Class: compiler and machine languaje
# project name: List of Users
# Program: userlist

from Tkinter import *
import ttk
import tkFont
import time
import datetime
import tkMessageBox
import mysql.connector

v0 = Tk()
v0.title("List of Users --- Security Door ----")
v0.geometry("650x350+400+150")



def search():
             global search_name
             search_name=SEARCH.get()
             print(str(search_name))
                          
             if search_name=='':
                                tkMessageBox.showinfo("Alert",message="It's empty")
             else:                    
                  tree.delete(*tree.get_children()) # It Function allows to clean our tree or Grid
                  
                  cursor=conexion.cursor()
                  sql2="""SELECT usercod,name,lastname,num_pass,status FROM users WHERE name=("%s") or lastname=("%s") or usercod=("%s");"""%((search_name),(search_name),(search_name))
                  cursor.execute(sql2)
                  result=cursor.fetchall()
                  for data in result:
                                     tree.insert('','end',values=(data))
                                     cursor.close()
                                                    
def reset():
            tree.delete(*tree.get_children())
            cursor=conexion.cursor()
            sql=""" select * from users """ # Sql string
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                               tree.insert('','end',values=(item[0],item[1],item[2],item[7],item[8])) #inserting in treeview or grid
                               cursor.close()



# ----------------- Creation of Grid or Treeview -----------------------------------
tree = ttk.Treeview(v0) # ttk library for object treeview 
tree["columns"]=("one","two","three","four","five") # numbers of columns
tree.column("one", width=80)
tree.column("two", width=80)
tree.column("three", width=80)
tree.column("four", width=80)
tree.column("five", width=80)
# Heading, columns's name
tree.heading("one", text="User-Code")
tree.heading("two", text="Name")
tree.heading("three",text="Lastname")
tree.heading("four",text="Password")
tree.heading("five",text="Status")

#Data base connection

conexion=mysql.connector.connect(
                                  host="localhost",
                                  user="root",
                                  password="meduza1",
                                  database="uth"
                                  )
# Creation of cursor
cursor=conexion.cursor()
sql=""" select * from users """ # Sql string
cursor.execute(sql)
result=cursor.fetchall()
for item in result:
                   tree.insert('','end',values=(item[0],item[1],item[2],item[7],item[8])) #inserting in treeview or grid
                   cursor.close()

tree.place(x=20,y=65) # Printing of treeview on the window

# ---------------------------------Treeview End ----------------------------------------

# -------------------------------- Labels and Buttons ---------------------------------------------
textfont=tkFont.Font(family="helvetica",size=18)
text_comment=tkFont.Font(family="helvetica",size=9)
label1=Label(v0,text="List of Users",font=textfont).place(x=80,y=20)
image_logo=PhotoImage(file="logouth.gif")
btn_logo=Button(v0,image=image_logo).place(x=19,y=2)
quit_image=PhotoImage(file="quit.png")
quit_button=Button(v0,image=quit_image,command=v0.destroy).place(x=561,y=287,height=60,width=60)
comment1=Label(v0,text="* To Observe: A=Active,I=Inactive",font=text_comment).place(x=21,y=287)
comment2=Label(v0,text="* Making Click on Grid ",font=text_comment).place(x=21,y=305)
comment3=Label(v0,text="** SEARCH:'User-code', 'Name' ,'Lastname' **",foreground="green",font=text_comment).place(x=21,y=320)
# ------------- SEARCH FIELD IN BD ------------------
SEARCH=StringVar()
label_search=Label(v0,text="Search:",font=text_comment).place(x=240,y=40)
textbox1=Entry(v0,textvariable=SEARCH,width=20).place(x=290,y=40)
# -------- SEARCH BUTTON ----------------------------
button1=Button(v0,text="SEARCH",command=search).place(x=465,y=35)
button2=Button(v0,text="RESET",command=reset).place(x=545,y=35)

v0.mainloop()
