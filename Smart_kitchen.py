import RPi.GPIO as GPIO
import time
from time import sleep
servo_pin= 13
#led_pin=25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)       #MQ2 Buzzer
GPIO.setup(14,GPIO.IN)        
#GPIO.setup(25,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
#pwm = GPIO.PWM(25,100)
GPIO.setup(servo_pin,GPIO.OUT)    #Servo motor out
#pwm = GPIO.PWM(servo_pin,50)
mq=0
#pwm.start(7)# DUST BIN
status=0
#pwm.start(status)

#GAS DETECTION
def gas(): 
mq= GPIO.input(14) 
print(mq)
if(mq==1):
GPIO.output(16, GPIO.HIGH) #mq2 high
print("GAS DETECTED")
GPIO.output(17,GPIO.HIGH) #buzzer high
GPIO.output(2,True)
print("LED ON") 
elif(mq==0): 
GPIO.output(16, GPIO.LOW) #mq2 low 
print("GAS NOT DETECTED")
GPIO.output(17,GPIO.LOW)  #not buzzer
GPIO.output(2,False)
print("LED OFF") 

return gas

'''def servo():
pwm.ChangeDutyCycle(2.0)
time.sleep(0.5)
pwm.ChangeDutyCycle(7.0)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()
return servo'''
def fan():
if(mq==1):
GPIO.output(3,True)
print("FAN ON")
time.sleep(1)
else:
GPIO.output(3,False)
print("FAN OFF")
time.sleep(2)


while True:
gas()
#servo()
fan()
#pwm.stop() 

