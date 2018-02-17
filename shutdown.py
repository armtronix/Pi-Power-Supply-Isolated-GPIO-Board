from time import sleep
import RPi.GPIO as GPIO  # added on 09/01/2018 by Naren
import os # added on 09/01/2018 by Naren
######For reboot and shutdown button input ########
gpio_pin_number_for_pi_on_off_input =35 #Gpio 19 pin 35
GPIO.setmode(GPIO.BOARD)

gpio_pin_number_for_pi_on_off_output =13 #Gpio 27  pin 13
#gpio_pin_number_for_pi_on_off =11 #gpio 13
GPIO.setup(gpio_pin_number_for_pi_on_off_output, GPIO.OUT) # added on 09/01/2018 for raspberry pi gpio 6 /pin 31 as output 
#GPIO.output(gpio_pin_number_for_pi_on_off_output, False) #added on 09/01/2018 for sacn indication by naren


#####For Shutdown inputs ###################
GPIO.setup(gpio_pin_number_for_pi_on_off_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(gpio_pin_number_for_pi_reboot_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    GPIO.wait_for_edge(gpio_pin_number_for_pi_on_off_input, GPIO.FALLING)
    #Use falling edge detection to see if pin is pulled 
    #low to avoid repeated polling
    GPIO.output(gpio_pin_number_for_pi_on_off_output, True) #added on 09/01/2018 for sacn indication by naren
#    time.sleep(0.5)
    os.system("sudo halt")
    #Send command to system to shutdown
except:
    pass

