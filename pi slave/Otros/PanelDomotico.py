# Declaracion de Librerias del Modulo tkinter
from Tkinter import *
from ttk import *
import tkFont
import tkMessageBox
#import pygame
import os
import subprocess
import sqlite3
import time
#pygame.mixer.init()
#pygame.mixer.music.load("/home/pi/PracticasTK/acceso1.mp3")
#sudo apt-get install timidity
################################################## VENTANA # 1 #############################################
# TOPLEVEL

def settings():
    global operator
    operator=operator+str(numbers)
    cod.set(operator)

def save():
         tab=StringVar()
         hi=horai.get()
         mi=mini.get()
         hf=horaf.get()
         mf=minf.get()
         dia="*"
         mes="*"
         ano="*"
         tab=" "
         user="root"
         path="/home/pi/activar.sh"
         path2="/home/pi/desactivar.sh"
         cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)
                 +''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
         print(str(cadena))
         tkMessageBox.showinfo("Save",message="Alarma Programada con Exito")
         os.system("/./home/pi/permiso.sh")
         pf=open(r'/etc/cron.d/tarea1','w')
         pf.write(cadena)
         pf.close()
         
         cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)
                  +''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
         print(str(cadena2))
         pf2=open(r'/etc/cron.d/tarea2','w')
         pf2.write(cadena2)
         pf2.close()
         os.system("/./home/pi/nopermiso.sh")
         pygame.mixer.music.load("/home/pi/PracticasTK/horarioprog.mp3")
         pygame.mixer.music.play()
        
def toplevel2():
    global horaih1,horaih2,horaih3,horaih4,horaih5,horaih6
    global horafh1,horafh2,horafh3,horafh4,horafh5,horafh6
    global minih1,minih2,minih3,minih4,minih5,minih6
    global minfh1,minfh2,minfh3,minfh4,minfh5,minfh6
    v2=Toplevel()
    v2.title("Configurar ON/OFF de Luces x Horario")
    v2.geometry("550x350+100+100")
    
    horaih1=StringVar()   
    minih1=StringVar()
    horafh1=StringVar()
    minfh1=StringVar()

    horaih2=StringVar()
    minih2=StringVar()
    horafh2=StringVar()
    minfh2=StringVar()

    horaih3=StringVar()
    minih3=StringVar()
    horafh3=StringVar()
    minfh3=StringVar()

    horaih4=StringVar()
    minih4=StringVar()
    horafh4=StringVar()
    minfh4=StringVar()

    horaih5=StringVar()
    minih5=StringVar()
    horafh5=StringVar()
    minfh5=StringVar()

    horaih6=StringVar()
    minih6=StringVar()
    horafh6=StringVar()
    minfh6=StringVar()

    textfont=tkFont.Font(family="Helvetica",size=11,weight="bold")
    textfont2=tkFont.Font(family="Helvetica",size=10,weight="bold")
    label1=Label(v2,text="PROGRAMAR ENCENDIDO Y APAGADO DE LUCES",font=textfont).place(x=70,y=05)
    labelon=Label(v2,text="- - - ON - - -").place(x=210,y=40)
    labeloff=Label(v2,text="- - - OFF - - -").place(x=360,y=40)
    labelhorai=Label(v2,text="Hora-ini").place(x=190,y=60)
    labelmini=Label(v2,text="Min-ini").place(x=260,y=60)
    labelhoraf=Label(v2,text="Hora-fin").place(x=330,y=60)
    labelhorai=Label(v2,text="Min-fin").place(x=410,y=60) 
    labelhab1=Label(v2,text="Habitacion -1-",font=textfont).place(x=70,y=80)
    labelhab2=Label(v2,text="Habitacion -2-",font=textfont).place(x=70,y=120)
    labelhab3=Label(v2,text="Habitacion -3-",font=textfont).place(x=70,y=160)
    labelhab4=Label(v2,text="Habitacion -4-",font=textfont).place(x=70,y=200)
    labelhab5=Label(v2,text="Habitacion -5-",font=textfont).place(x=70,y=240)
    labelhab6=Label(v2,text="Habitacion -6-",font=textfont).place(x=70,y=280)

    texthoraih1=Entry(v2,textvariable=horaih1,width=7).place(x=190,y=80)
    textminih1=Entry(v2,textvariable=minih1,width=7).place(x=260,y=80)
    texthorafh1=Entry(v2,textvariable=horafh1,width=7).place(x=330,y=80)
    textminfh1=Entry(v2,textvariable=minfh1,width=7).place(x=410,y=80)
 
    texthoraih2=Entry(v2,textvariable=horaih2,width=7).place(x=190,y=120)
    textminih2=Entry(v2,textvariable=minih2,width=7).place(x=260,y=120)
    texthorafh2=Entry(v2,textvariable=horafh2,width=7).place(x=330,y=120)
    textminfh2=Entry(v2,textvariable=minfh2,width=7).place(x=410,y=120)        

    texthoraih3=Entry(v2,textvariable=horaih3,width=7).place(x=190,y=160)
    textminih3=Entry(v2,textvariable=minih3,width=7).place(x=260,y=160)
    texthorafh3=Entry(v2,textvariable=horafh3,width=7).place(x=330,y=160)
    textminfh3=Entry(v2,textvariable=minfh3,width=7).place(x=410,y=160)

    texthoraih4=Entry(v2,textvariable=horaih4,width=7).place(x=190,y=200)
    textminih4=Entry(v2,textvariable=minih4,width=7).place(x=260,y=200)
    texthorafh4=Entry(v2,textvariable=horafh4,width=7).place(x=330,y=200)
    textminfh4=Entry(v2,textvariable=minfh4,width=7).place(x=410,y=200)

    texthoraih5=Entry(v2,textvariable=horaih5,width=7).place(x=190,y=240)
    textminih5=Entry(v2,textvariable=minih5,width=7).place(x=260,y=240)
    texthorafh5=Entry(v2,textvariable=horafh5,width=7).place(x=330,y=240)
    textminfh5=Entry(v2,textvariable=minfh5,width=7).place(x=410,y=240)
    
    texthoraih6=Entry(v2,textvariable=horaih6,width=7).place(x=190,y=280)
    textminih6=Entry(v2,textvariable=minih6,width=7).place(x=260,y=280)
    texthorafh6=Entry(v2,textvariable=horafh6,width=7).place(x=330,y=280)
    textminfh6=Entry(v2,textvariable=minfh6,width=7).place(x=410,y=280)


    v2.mainloop()
    
              
                                    
def toplevel():
    # Las variables Globales siempre deben de declarse al inicio de cada metodo o funcion
    # Para que no generen advertencias o warning ejemplo:syntaxwarning name is assigned to before global declaration
    global horai
    global horaf
    global mini
    global minf
    v1=Toplevel()
    v1.title("Configurar Alarma x Horarios")
    v1.geometry("450x300+200+200")
    mini=StringVar()
    minf=StringVar()
    horai=StringVar()
    horaf=StringVar()
    # Declarar Variables Globales para ser usadas dentro de cualquier funcion o metodo
       
    texttop=tkFont.Font(family="Helvetica",size=10,weight="bold")
    texttop2=tkFont.Font(family="Helvetica",size=9,weight="bold")
    label1top=Label(v1,text="HORARIO DE ACTIVACION & DESACTIVACION DE ALARMA",font=texttop).place(x=50,y=10)
    label2top=Label(v1,text="HORA INICIAL :",font=texttop2).place(x=110,y=70)

    caja2=Entry(v1,textvariable=horai,width=20).place(x=215,y=70)

    label3top=Label(v1,text="MINUTO INICIAL :",font=texttop2).place(x=110,y=110)
    TextBox2=Entry(v1,textvariable=mini,width=20).place(x=215,y=110)
    label4top=Label(v1,text="HORA FINAL :",font=texttop2).place(x=110,y=150)
    TextBox3=Entry(v1,textvariable=horaf,width=20).place(x=215,y=150)
    label5top=Label(v1,text="MINUTO FINAL :",font=texttop2).place(x=110,y=190)
    TextBox4=Entry(v1,textvariable=minf,width=20).place(x=215,y=190)

    # Boton Guardar
    imgsave=PhotoImage(file="guardar.gif")
    botosettings=Button(v1,image=imgsave,command=save,width=50).place(x=215,y=220,height=50)
    botonclose=Button(v1,text="Cerrar", command=v1.destroy).place(x=295,y=220,height=50)
    # Reloj Time
    def update():
        current=time.strftime("%H:%M:%S")
        labelTiempo=Label(v1,text=" -- Tiempo --").place(x=110,y=230) 
        labeltime=Label(v1,text=current).place(x=120,y=250)
        v1.after(1000,update)
    update()
    v1.mainloop()
    
###############################################################################################################

##############################################################################

# Definiendo los metodos o funciones para cada Foco(Gpio)

def Foco1on():
    tkMessageBox.showinfo("Habitacion 1",message="Foco 1 Encendido")
def Foco1off():
    tkMessageBox.showinfo("Habitacion 2",message="Foco 2 Apagado")
    
def Foco2on():
    tkMessageBox.showinfo("Habitacion 2",message="Foco 2 Encendido")
def Foco2off():
    tkMessageBox.showinfo("Habitacion 2",message="Foco 2 Apagado")
    
def Foco3on():
    tkMessageBox.showinfo("Habitacion 3",message="Foco 3 Encendido")
def Foco3off():
    tkMessageBox.showinfo("Habitacion 3",message="Foco 3 Apagado")
    
def Foco4on():
    tkMessageBox.showinfo("Habitacion 4",message="Foco 4 Encendido")
def Foco4off():
    tkMessageBox.showinfo("Habitacion 4",message="Foco 4 Apagado")

def Foco5on():
    tkMessageBox.showinfo("Habitacion 5",message="Foco 5 Encendido")
def Foco5off():
    tkMessageBox.showinfo("Habitacion 5",message="Foco 5 Apagado")

def Foco6on():
    tkMessageBox.showinfo("Habitacion 6",message="Foco 6 Encendido")
def Foco6off():
    tkMessageBox.showinfo("Habitacion 6",message="Foco 6 Apagado")
    
# Metodo para concatenar numeros en la caja1-variable->cod, al presionar diferentes botones
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    cod.set(operator)

def ValidarClave():
    numero=StringVar()
    estado=StringVar()
    numero=operator
    db=sqlite3.connect('/home/pi/PracticasTK/domotic.db')
    c=db.cursor()
    
    c.execute('SELECT * FROM LOGIN WHERE PASSWORD=? and ESTADO=?',(numero,'A'))
    if c.fetchall():
        tkMessageBox.showinfo("ALARMA ACTIVADA",message="ALARMA ACTIVADA")
        # llamar una funcion dentro de otra funcion.
        textconf=tkFont.Font(family="Helvetica",size=9,weight="bold")
        estado1=Label(v0,text="ACTIVADA",width=16,background="green",font=textconf).place(x=710,y=80)
        #os.system("start acceso1.wav")
        #pygame.mixer.music.play()
        pygame.mixer.music.load("/home/pi/PracticasTK/alarmactivada.mp3")
        pygame.mixer.music.play()    

    c.execute('SELECT * FROM LOGIN WHERE PASSWORD=? and ESTADO=?',(numero,'D'))
    if c.fetchall():
        textconf=tkFont.Font(family="Helvetica",size=9,weight="bold")
        tkMessageBox.showinfo("ALARMA DESACTIVADA",message="ALARMA DESACTIVADA")
        btnestadoOFF=PhotoImage(file="of.gif")
        estado2=Label(v0,text="DESACTIVADA",width=16,background="red",font=textconf).place(x=710,y=80)
        #llamar una funcion dentro de otra funcion.
        ## btnClsCaja1()
        pygame.mixer.music.load("/home/pi/PracticasTK/alarmadesactivada.mp3")
        pygame.mixer.music.play()
        c.close()

    if numero=='':
              textconf=tkFont.Font(family="Helvetica",size=9,weight="bold")
              estado3=Label(v0,text="NO CONFIGURADO",width=16,background="gray",font=textconf).place(x=710,y=80)
              #subprocess.call("C:\Python33\Practicas TK\tkcalc.py")
              pygame.mixer.music.load("/home/pi/PracticasTK/alarmanoconfig.mp3")
              pygame.mixer.music.play()

    if numero!='1900' and numero!='1981':
              textconf=tkFont.Font(family="Helvetica",size=9,weight="bold")
              estado4=Label(v0,text="NO CONFIGURADO",width=16,background="gray",font=textconf).place(x=710,y=80)
              pygame.mixer.music.load("/home/pi/PracticasTK/alarmanoconfig.mp3")
              pygame.mixer.music.play()   
                 
def btnClsCaja1():
    global operator
    operator=""
    cod.set(operator)

# Defincion de la Ventana Principal (ventana Padre)        
v0=Tk()
v0.geometry("850x517+0+0")
v0.title("APP DOMOTICSECURITY SYSTEM")

# Asignar imagenes a Foco1
bgtext1 = tkFont.Font(family="Helvetica", size=12, weight="bold")
label1=Label(v0,text="HABITACION  1",font=bgtext1).place(x=70,y=10)
imgboton1=PhotoImage(file="on.png")
boton1=Button(v0,image=imgboton1,command=Foco1on).place(x=20,y=50,height=100,width=100)
imgboton1b=PhotoImage(file="off.png")
boton1b=Button(v0,image=imgboton1b,command=Foco1off,width=100).place(x=140,y=50,height=100)

# Asignar imagenes a Foco2
bgtext2= tkFont.Font(family="Helvetica", size=12, weight="bold")
label2=Label(v0,text="HABITACION  2",font=bgtext2).place(x=70,y=160)
imgboton2=PhotoImage(file="on.png")
boton2=Button(v0,image=imgboton2,command=Foco2on,width=100).place(x=20,y=205,height=100)
imgboton2b=PhotoImage(file="off.png")
boton2b=Button(v0,image=imgboton2b,command=Foco2off,width=100).place(x=140,y=205,height=100)

# Asignar Imagen a Foco3
bgtext3= tkFont.Font(family="Helvetica", size=12, weight="bold")
label3=Label(v0,text="HABITACION  3",font=bgtext3).place(x=70,y=315)
imgboton3=PhotoImage(file="on.png")
boton3=Button(v0,image=imgboton3,command=Foco3on,width=100).place(x=20,y=360,height=100)
imgboton3b=PhotoImage(file="off.png")
boton3b=Button(v0,image=imgboton3b,command=Foco3off,width=100).place(x=140,y=360,height=100)

################################ Habitacion 4,5,6 ##########################################

# Asignar Imagen a Foco4
bgtext4=tkFont.Font(family="Helvetica", size=12, weight="bold")
label4=Label(v0,text="HABITACION  4",font=bgtext4).place(x=320,y=10)
imgboton4=PhotoImage(file="on.png")
boton4=Button(v0,image=imgboton4,command=Foco4on,width=100).place(x=280,y=50,height=100)
imgboton4b=PhotoImage(file="off.png")
boton4b=Button(v0,image=imgboton4b,command=Foco4off,width=100).place(x=400,y=50,height=100)

#asignar Imagen a Foco5
bgtext5=tkFont.Font(family="Helvetica",size=12,weight="bold")
label5=Label(v0,text="HABITACION  5",font=bgtext5).place(x=320,y=160)
imgboton5=PhotoImage(file="on.png")
boton5=Button(v0,image=imgboton5,command=Foco5on,width=100).place(x=280,y=205,height=100)
imgboton5b=PhotoImage(file="off.png")
boton5b=Button(v0,image=imgboton5b,command=Foco5off,width=100).place(x=400,y=205,height=100)

#asignar Imagen a Foco6
bgtext6=tkFont.Font(family="Helvetica",size=12,weight="bold")
label6=Label(v0,text="HABITACION  6",font=bgtext6).place(x=320,y=315)
imgboton6=PhotoImage(file="on.png")
boton6=Button(v0,image=imgboton6,command=Foco6on,width=100).place(x=280,y=360,height=100)
imgboton6b=PhotoImage(file="off.png")
boton6b=Button(v0,image=imgboton6b,command=Foco6off,width=100).place(x=400,y=360,height=100)

# Asignar Imagen a Alarma
bgtext7=tkFont.Font(family="Helvetica",size=12,weight="bold")
label7=Label(v0,text="ALARMA-SECTORIAL",font=bgtext7).place(x=560,y=7)
imgboton7=PhotoImage(file="icon.png")
boton7=Button(v0,image=imgboton7,width=100).place(x=590,y=50,height=100)

#Asignar Imagen a Boton settings
imgsettings=PhotoImage(file="config.png")
botosettings=Button(v0,image=imgsettings,command=toplevel,width=50).place(x=736,y=01,height=50)

#Asignar imagen a Botton setting2 focos
imgsettings2=PhotoImage(file="config.png")
botonsettings2=Button(v0,image=imgsettings2,command=toplevel2,widt=50).place(x=506,y=01,height=50)

# Caja de Texto password
cod=StringVar()
operator=""
caja1=Entry(v0,textvariable=cod,width=20,font=bgtext7,show="*",state='disabled').place(x=547,y=170)

# Teclado Numerico 1-9
# definicion de la fuente y dimesiones del texto usado en los numeros de los botones
bgtext=tkFont.Font(family="Helvetica",size=13,weight="bold")
# boton numero 1
btnum1=Button(v0,text="1",command=lambda:btnClick(1),width=5).place(x=547,y=210)

# boton numero 2
btnum2=Button(v0,text="2",command=lambda:btnClick(2),width=5).place(x=614,y=210)

# boton numero 3
btnum3=Button(v0,text="3",command=lambda:btnClick(3),width=5).place(x=680,y=210)

# boton numero 4
btnum4=Button(v0,text="4",command=lambda:btnClick(4),width=5).place(x=547,y=270)

# boton numero 5
btnum5=Button(v0,text="5",command=lambda:btnClick(5),width=5).place(x=614,y=270)

# boton numero 6
btnum6=Button(v0,text="6",command=lambda:btnClick(6),width=5).place(x=680,y=270)

# boton numero 7
btnum7=Button(v0,text="7",command=lambda:btnClick(7),width=5).place(x=547,y=330)

# boton numero 8
btnum8=Button(v0,text="8",command=lambda:btnClick(8),width=5).place(x=614,y=330)

# boton numero 9
btnum9=Button(v0,text="9",command=lambda:btnClick(9),width=5).place(x=680,y=330)

# boton numero 0
btnum0=Button(v0,text="0",command=lambda:btnClick(0),width=5).place(x=547,y=390)

# boton Enter
btnenter=Button(v0,text="<---/ ENTER",command=ValidarClave,width=12).place(x=614,y=390)

# boton Limpiar C
btncls=Button(v0,text="C",command=btnClsCaja1,width=5).place(x=614,y=449)


v0.mainloop()
 
    

