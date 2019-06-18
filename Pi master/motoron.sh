#!/bin/bash
sshpass -p "soreal1997" ssh -l  pi 172.20.10.6 "sudo /./home/pi/motoron.sh"
#echo 27 > /sys/class/gpio/export
#echo out > /sys/class/gpio/gpio27/direction
#echo 0 > /sys/class/gpio/gpio27/value

