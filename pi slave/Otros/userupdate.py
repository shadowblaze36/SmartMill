# Developer: Cubillax
# date: 9/12/2018
# Class: compiler and machine languaje
# project name: Security Door
# Program: Update

from Tkinter import *
from ttk import *
import tkFont
import os
import tkMessageBox
import time
import mysql.connector
import datetime

v0=Tk()
v0.title("UserUpdate --- Security Door ---")
v0.geometry("500x370+400+150")

# ----- Methods or functions
def find():
           global cod
           cod=codigo.get()
           conexion2=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="meduza1",
                                            database="uth"
                                           )
           cursor2=conexion2.cursor()
           sql2=""" select * from users where usercod=("%s");"""%(cod)
           cursor2.execute(sql2)
           result=cursor2.fetchall()
           for item in result:
                              field1=item[1]
                              field2=item[2]
                              field3=item[3]
                              field5=item[5]
                              field6=item[6]
                              field7=item[7]
                              field8=item[8]
                                                         
                              name.set(field1)
                              lastname.set(field2)
                              startdate.set(field3)
                              job.set(field5)
                              journal.set(field6)
                              password.set(field7)
                              retry.set(field7)
                              status.set(field8)
                              
def save():
           codigo1=codigo.get()
           name1=name.get()
           lastname1=lastname.get()
           startdate1=startdate.get()
           job1=job.get()
           journal1=journal.get()
           password1=password.get()
           retry1=retry.get()
           status1=status.get()
           #--- field's validation-----
           if password1!=retry1:
                               tkMessageBox.showinfo("save",message="Different Password")
                               
           elif password1=='':
                              tkMessageBox.showinfo("save",message="Empty password")
           elif retry1=='':
                           tkMessageBox.showinfo("save",message="Empty retry password")
           elif name1=='':
                           tkMessageBox.showinfo("save",message="Empty name")
           elif lastname1=='':
                             tkMessageBox.showinfo("save",message="Empty lastname")
           elif job1=='':
                         tkMessageBox.showinfo("save",message="Empty job")
           
           elif journal1=='':
                             tkMessageBox.showinfo("save",message="Empty journal")
           else:                 
                            
                conexion=mysql.connector.connect(
                                                 host="localhost",
                                                 user="root",
                                                 password="meduza1",
                                                 database="uth"
                                                )
                cursor1=conexion.cursor()
                sql1="""update users set name=("%s"),
                                      lastname=("%s"),
                                      update_date=("%s"),
                                      job=("%s"),
                                      journal=("%s"),
                                      num_pass=("%s"),
                                      status=("%s")
                                      where usercod=("%s");"""%(str(name1),str(lastname1),str(startdate1),str(job1),str(journal1),str(password1),str(status1),str(codigo1))
                cursor1.execute(sql1)                         
                conexion.commit()

                label_save=Label(v0,text="<--Modified Successfully-->",font=text_comment).place(x=315,y=315)
                # ---- cleaning fields --------
                name.set(str(''))
                lastname.set(str(''))
                startdate.set(str(''))
                job.set(str(''))
                journal.set(str(''))
                password.set(str(''))
                retry.set(str(''))
                status.set(str(''))
        
                # --- Only for verifying on terminal -----
                print "Hello guys"
                print(str(name1))
                print(str(lastname1))
                print(str(startdate1))
                print(str(startdate1))
                print(str(job1))
                print(str(journal1))
                print(str(password1))
                print(str(status1))
           

# Logos and labels
textfont=tkFont.Font(family="Helvetica",size=14)
text_comment=tkFont.Font(family="Helvetica",size=10)
text_title=tkFont.Font(family="Helvetica",size=15)
imagen_logo=PhotoImage(file="logouth.gif")
btn_logo=Button(v0,image=imagen_logo).place(x=10,y=10,height=65,width=65)
label=Label(v0,text="Modifying Users",font=text_title).place(x=200,y=10)

# Labels and textbox
label0=Label(v0,text="Codigo:",font=textfont).place(x=200,y=45)
label1=Label(v0,text="* Name :",font=textfont).place(x=10,y=90)
label2=Label(v0,text="* Lastname :",font=textfont).place(x=10,y=120)
label3=Label(v0,text=" StartDate :",font=textfont).place(x=10,y=150)
label4=Label(v0,text="* Kind of Job:",font=textfont).place(x=10,y=180)
label5=Label(v0,text="* Journal :",font=textfont).place(x=10,y=210)
label6=Label(v0,text="* Password:",font=textfont).place(x=10,y=240)
label7=Label(v0,text="* Retry Password:",font=textfont).place(x=10,y=270)
comment1=Label(v0,text=" * Campos Obligatorios",font=text_comment).place(x=10,y=310)
comment2=Label(v0,text="A=Active,I=Inactive",font=text_comment).place(x=21,y=325)
label8=Label(v0,text="Estado:",font=textfont).place(x=200,y=310)

# Definition of variables
codigo=StringVar()
name=StringVar()
lastname=StringVar()
startdate=StringVar()
job=StringVar()
journal=StringVar()
password=StringVar()
retry=StringVar()
status=StringVar()
# now date
datehour=datetime.datetime.now()
startdate.set(str(datehour))

# ---- TextBox -----
textbox0=Entry(v0,textvariable=codigo,width=7).place(x=270,y=50)
textbox1=Entry(v0,textvariable=name,width=20).place(x=120,y=95)
textbox2=Entry(v0,textvariable=lastname,width=20).place(x=120,y=125)
textbox3=Entry(v0,textvariable=startdate,width=20).place(x=120,y=155)
textbox4=Entry(v0,textvariable=job,width=20).place(x=120,y=185)
textbox5=Entry(v0,textvariable=journal,width=20).place(x=120,y=215)
textbox6=Entry(v0,textvariable=password,width=20).place(x=120,y=245)
textbox7=Entry(v0,textvariable=retry,width=20).place(x=165,y=275)
textbox8=Entry(v0,textvariable=status,width=2).place(x=270,y=314)

# ----- Buttons -----
find_image=PhotoImage(file="list.gif")
find_button=Button(v0,image=find_image,command=find).place(x=370,y=95,height=60,width=60)

save_image=PhotoImage(file="guardar.gif")
save_button=Button(v0,image=save_image,command=save).place(x=370,y=155,height=60,width=60)

quit_image=PhotoImage(file="quit.png")
quit_button=Button(v0,image=quit_image,command=v0.destroy).place(x=370,y=215,height=60,width=60)

v0.mainloop()
