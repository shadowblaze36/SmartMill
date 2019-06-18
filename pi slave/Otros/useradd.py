# Developer: Cubillax
# date: 6/12/2018
# Class: compiler and machine languaje
# project name: Security Door

from Tkinter import *
from ttk import *
import tkFont
import os
import tkMessageBox
import time
import mysql.connector
import datetime

v0=Tk()
v0.title("Useradd --- Security Door ---")
v0.geometry("500x350+400+150")

# ----- Methods or functions
def save():
           name1=name.get()
           lastname1=lastname.get()
           startdate1=startdate.get()
           job1=job.get()
           journal1=journal.get()
           password1=password.get()
           retry1=retry.get()
           status='A'
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
                sql1="""insert into users (name,
                                      lastname,
                                      start_date,
                                      update_date,
                                      job,
                                      journal,
                                      num_pass,
                                      status
                                     )
                values               (%s,
                                      %s,
                                      %s,
                                      %s,
                                      %s,
                                      %s,
                                      %s,
                                      %s)"""
                variables=(str(name1),str(lastname1),str(startdate1),str(startdate1),str(job1),str(journal1),str(password1),str(status))
                #cursor1.execute(sql1,(str(name1),str(lastname1),str(startdate1),str(startdate1),str(job1),str(journal1),str(password1)))
                cursor1.execute(sql1,variables)                         
                conexion.commit()

                label_save=Label(v0,text="Saved Successfully",font=textfont).place(x=250,y=320)
                # ---- cleaning fields --------
                name.set(str(''))
                lastname.set(str(''))
                startdate.set(str(''))
                job.set(str(''))
                journal.set(str(''))
                password.set(str(''))
                retry.set(str(''))
                # --- Only for verifying on terminal -----
                print "Hello guys"
                print(str(name1))
                print(str(lastname1))
                print(str(startdate1))
                print(str(startdate1))
                print(str(job1))
                print(str(journal1))
                print(str(password1))
           

# Logos and labels
textfont=tkFont.Font(family="Helvetica",size=14)
text_comment=tkFont.Font(family="Helvetica",size=10)
text_title=tkFont.Font(family="Helvetica",size=15)
imagen_logo=PhotoImage(file="logouth.gif")
btn_logo=Button(v0,image=imagen_logo).place(x=10,y=10,height=65,width=65)
label=Label(v0,text="Adding Users",font=text_title).place(x=200,y=30)

# Labels and textbox

label1=Label(v0,text="* Name :",font=textfont).place(x=10,y=90)
label2=Label(v0,text="* Lastname :",font=textfont).place(x=10,y=120)
label3=Label(v0,text=" StartDate :",font=textfont).place(x=10,y=150)
label4=Label(v0,text="* Kind of Job:",font=textfont).place(x=10,y=180)
label5=Label(v0,text="* Journal :",font=textfont).place(x=10,y=210)
label6=Label(v0,text="* Password:",font=textfont).place(x=10,y=240)
label7=Label(v0,text="* Retry Password:",font=textfont).place(x=10,y=270)
comment1=Label(v0,text=" * Campos Obligatorios",font=text_comment).place(x=10,y=310)

# Definition of variables
name=StringVar()
lastname=StringVar()
startdate=StringVar()
job=StringVar()
journal=StringVar()
password=StringVar()
retry=StringVar()
# now date
datehour=datetime.datetime.now()
startdate.set(str(datehour))


# ---- TextBox -----
textbox1=Entry(v0,textvariable=name,width=20).place(x=120,y=95)
textbox2=Entry(v0,textvariable=lastname,width=20).place(x=120,y=125)
textbox3=Entry(v0,textvariable=startdate,width=20).place(x=120,y=155)
textbox4=Entry(v0,textvariable=job,width=20).place(x=120,y=185)
textbox5=Entry(v0,textvariable=journal,width=20).place(x=120,y=215)
textbox6=Entry(v0,textvariable=password,width=20).place(x=120,y=245)
textbox7=Entry(v0,textvariable=retry,width=20).place(x=165,y=275)


# ----- Buttons -----
save_image=PhotoImage(file="guardar.gif")
save_button=Button(v0,image=save_image,command=save).place(x=370,y=95,height=60,width=60)
quit_image=PhotoImage(file="quit.png")
quit_button=Button(v0,image=quit_image,command=v0.destroy).place(x=370,y=155,height=60,width=60)



v0.mainloop()


