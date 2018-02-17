from time import sleep
import RPi.GPIO as GPIO  # added on 09/01/2018 by Naren
import os # added on 09/01/2018 by Naren
######For reboot and shutdown button input ########
GPIO.setmode(GPIO.BOARD)

##########   OUTPUTS  ############################### 
gpo_pin_number_15 =15 #gpio 22
gpo_pin_number_13 =13 #gpio 11
gpo_pin_number_11 =11 #gpio 27
gpo_pin_number_07 =7 #gpio 07

GPIO.setup(gpo_pin_number_15, GPIO.OUT)  
GPIO.setup(gpo_pin_number_13, GPIO.OUT)  
GPIO.setup(gpo_pin_number_11, GPIO.OUT)  
GPIO.setup(gpo_pin_number_07, GPIO.OUT)  


##########   INPUTS ################################# 

gpi_pin_number_26 =37 #gpio 26
gpi_pin_number_13 =33 #gpio 13
gpi_pin_number_19 =35 #gpio 19
gpi_pin_number_06 =31 #gpio 06
 



while True:
    GPIO.output(gpo_pin_number_15, True)
    sleep(1*1)
    GPIO.output(gpo_pin_number_13, True)
    sleep(1*1)
    GPIO.output(gpo_pin_number_11, True)
    sleep(1*1)
    GPIO.output(gpo_pin_number_07, True)
    sleep(1*1)
    GPIO.output(gpo_pin_number_15, False)
    GPIO.output(gpo_pin_number_13, False)
    GPIO.output(gpo_pin_number_11, False)
    GPIO.output(gpo_pin_number_07, False)
    sleep(1*1)
