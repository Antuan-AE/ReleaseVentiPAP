try:
    import time
    import os 
    import RPi.GPIO as GPIO    
except RuntimeError:
    print("RPi.GPIO Library has not been loaded!" +\
          "Try using superuser privilage (sudo) on loading " +\
          "the script...")
    

DISPLAY_BACKLIGHT = 40
HIGH = 1
LOW = 0

GPIO.setwarnings(False)

#Set GPIO to BCM numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DISPLAY_BACKLIGHT, GPIO.OUT)
GPIO.output(DISPLAY_BACKLIGHT, GPIO.LOW)