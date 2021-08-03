try:
    import time
    import os 
    import RPi.GPIO as GPIO    
except RuntimeError:
    print("RPi.GPIO Library has not been loaded!" +\
          "Try using superuser privilage (sudo) on loading " +\
          "the script...")
    

POWER_BUTTOM_DISABLED = 29
DATA_ENABLE = 32
POWER_BUTTOM_ENABLED = 16
HIGH = 1
LOW = 0

GPIO.setwarnings(False)

#Set GPIO to BCM numbering
GPIO.setmode(GPIO.BOARD)  

GPIO.setup(POWER_BUTTOM_DISABLED, GPIO.OUT)
GPIO.setup(DATA_ENABLE, GPIO.OUT)
GPIO.setup(POWER_BUTTOM_ENABLED, GPIO.OUT)

GPIO.output(POWER_BUTTOM_DISABLED, GPIO.HIGH)
GPIO.output(DATA_ENABLE, GPIO.HIGH)
time.sleep(1)
GPIO.output(POWER_BUTTOM_DISABLED, GPIO.LOW)
GPIO.output(DATA_ENABLE, GPIO.HIGH)
GPIO.output(POWER_BUTTOM_ENABLED, GPIO.HIGH)

#GPIO.cleanup()


#Check output status
# os.system("echo 29 > /sys/class/gpio/export")
# 
# # try:
#     open("/sys/class/gpio/gpio29/value") as pin:
#         status = pin.read(1)
# #         
# #     except:
# #         print("Remember to export the pin first!")
# #         status = "Unknown"
# #         
#     print(status)
            
