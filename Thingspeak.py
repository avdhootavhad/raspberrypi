import thingspeak
import time import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(2,GPIO.OUT) #GPIO 2 -> Red LED as output 
GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input 
count = 0   
channel_id = 10***85 # put here the ID of the channel you created before 
write_key = 'ZLKA***3KPJ' # update the "WRITE KEY"   
def measure(channel):     
try:         # update the value         
response = channel.update({'field1': count})     
except:           
 print("connection failure") 
 if __name__ == "__main__":        
 channel = thingspeak.Channel(id=channel_id,api_key=write_key) 
while 1:    
 if(GPIO.input(14)==True): #object is far away         
GPIO.output(2,True) #Red led ON         
print("LED ON")         
time.sleep(1)         
 if(GPIO.input(14)==False): #object is near         
GPIO.output(2,False) # Red led OFF        
 print("LED OFF")         
time.sleep(1)    
count += 1     
measure(channel)           
  time.sleep(15)
