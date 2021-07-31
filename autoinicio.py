'''
Created on jul 7, 2017

@author: chamizo
'''
import os,sys
import commands
 
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


comando = "ps -ef | grep VentiApp"
estado = str(commands.getoutput(comando)).split('\n')
est = 0
for i in range(0,len(estado)):
        if not "grep" in estado[i]:
                est = 1
#print est
if est == 0:
        comando1 = "sudo nice -n-20 ./VentiApp"
        commands.getoutput(comando1)
#        os.system("sudo python /home/pi/VentiApp/scripts/shutdownbuttons.py &")
