#!/usr/bin/python3
import subprocess
import time
import pygame
import RPi.GPIO as GPIO

#pygame.mixer.music.load("/home/pi/Desktop/prueba/beep.mp3")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR = 23
GPIO.setup(GPIO_PIR,GPIO.IN)

num=0
status0 = 0
status1 = 0
try:
       while True:
               status0 = 0
               print "Listo para comenzar! xyz"
               while True:
                       status0 = GPIO.input(GPIO_PIR)
                       if status0==1 and status1==0:
                               num=num+1
                               print "Atencion, se ha detectado movimiento ",num,""
                               #pygame.mixer.music.play()
                               status1=1
 			       #subprocess.call("/./home/pi/proyecto/foto2.sh")
                               subprocess.call("/./home/pi/sirenaon.sh")
           
                       elif status0==0 and status1==1:
                                       print "Listo para comenzar!"
                                       status1=0
                                       time.sleep(0.01)
except KeyboardInterrupt:
       GPIO.cleanup()   
                       

                 



