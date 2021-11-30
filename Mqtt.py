##MQtt as a publisher

import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 14
GPIO_ECHO = 15
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
sensor = Adafruit_DHT.DHT11
channelID="1545849"
apikey="FTC9H6A4USKW5WHK"

tTransport_mqtt="tcp"
tport=1883
tTls=None

mqtt_Host="mqtt.thingspeak.com"
topic_1="channels/"+channelID+"/publish/"+apikey

while True:
	GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
 
	StartTime = time.time()
	StopTime = time.time()
 
    # save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
 
    # save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
 
    # time difference between start and arrival
	TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2
	tPayload="field1="+str(distance)
	print(distance)
	publish.single(topic_1,payload=tPayload,hostname=mqtt_Host,port=tport,tls=tTls,transport=tTransport_mqtt)
	print("Data publish succesful")
