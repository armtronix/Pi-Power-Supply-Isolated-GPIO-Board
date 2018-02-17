from time import sleep
import RPi.GPIO as GPIO  # added on 09/01/2018 by Naren
import os # added on 09/01/2018 by Naren
######For reboot button input ########
gpio_pin_number_for_pi_reboot_input =37 #37 is pin number and 26 is gpio
GPIO.setmode(GPIO.BOARD)
gpio_pin_number_for_pi_reboot_output =13 #13 id pin number and 27 is gpio
GPIO.setup(gpio_pin_number_for_pi_reboot_output, GPIO.OUT) # added on 09/01/2018 for raspberry pi gpio 6 /pin 31 as output 
#GPIO.output(gpio_pin_number_for_pi_reboot_output, False) #added on 09/01/2018 for sacn indication by naren


#####For Shutdown inputs ###################
GPIO.setup(gpio_pin_number_for_pi_reboot_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    GPIO.wait_for_edge(gpio_pin_number_for_pi_reboot_input, GPIO.FALLING)
    #Use falling edge detection to see if pin is pulled 
    #low to avoid repeated polling
    GPIO.output(gpio_pin_number_for_pi_reboot_output, True) #added on 09/01/2018 for sacn indication by naren
    os.system("sudo reboot")
    #Send command to system to shutdown
except:
    pass

