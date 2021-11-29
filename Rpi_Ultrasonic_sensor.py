import RPi.GPIO as GPIO

import time

 

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)



servo_pin= 13

GPIO_TRIGGER = 18

GPIO_ECHO = 24

GPIO_led= 2

 

#set GPIO direction (IN / OUT)

GPIO.setup(servo_pin,GPIO.OUT)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(GPIO_led,GPIO.OUT)

c=0



pwm=GPIO.PWM(servo_pin,50)

pwm.start(7)

 

def distance():

    # set Trigger to HIGH

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

 

    return distance 

    

 

if __name__ == '__main__':

    try:

        while True:

            dist = distance()

            print ("Measured Distance = %.1f cm" % dist)

            if dist <= 10:

               GPIO.output(GPIO_led,True)

               pwm.ChangeDutyCycle(7.0) #rotate to 90 degree

               time.sleep(0.5)

            else:

                GPIO.output(GPIO_led,False)

                pwm.ChangeDutyCycle(2.0) #rotate to 0 degrees

                time.sleep(0.5)

            time.sleep(1) 

  

 

        # Reset by pressing CTRL + C

    except KeyboardInterrupt:

        print("Measurement stopped by User")

        pwm.ChangeDutyCycle(0)  #this is present jitter

        pwm.stop()

        GPIO.cleanup()

