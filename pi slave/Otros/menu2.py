#DECLARACION DE LIBRERIAS DEL MODULO TKINTER
from Tkinter import*
from ttk import*
import tkFont
import tkMessageBox
#import pygame
import os
import subprocess
import sqlite3
import time

import mysql.connector
####################  DEFINICION DE LA VENTANA PRINCIPAL (VENTANA PADRE)  ######################
v1=Tk()
v1.geometry("800x600+300+100")
v1.title("UTH SMARTDOOR")
def on():
               print "hola ON"

def off():
                print "hola OFF"

title_text=tkFont.Font(family="Helvetica",size=15,weight="bold")
label50=Label(v1,text="SMARTDOOR SYSTEM",font=title_text).place(x=275,y=10)
############################### Asignar imagenes a Raspi ######################################
bgtext1 = tkFont.Font(family="Helvetica",size=12,weight="bold")
label1=Label(v1,text="--- DOOR 108 ---",font=bgtext1).place(x=110,y=50)

# --------------------- Door image ------------------------------------------------
imgdoorfinal=PhotoImage(file="doorfinal.png")
button_door=Button(v1,image=imgdoorfinal).place(x=20,y=70,width=300,height=400)
#---------------------------Settings-----------------------------------------------
imgsettings=PhotoImage(file="settings3.gif")
button_settings=Button(v1,image=imgsettings).place(x=220,y=495,width=100,height=100)

imgboton1_on=PhotoImage(file="on.gif")
boton1_on=Button(v1,image=imgboton1_on,command=on,width=100).place(x=20,y=495,height=100)
############################### Asignar imagenes a Security Door  ##############################
bgtext2=tkFont.Font(family="Helvetica",size=12,weight="bold")
imgboton2_off=PhotoImage(file="off.gif")
boton2_off=Button(v1,image=imgboton2_off,command=off,width=100).place(x=140,y=495,height=100)
v1.mainloop()
