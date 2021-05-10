import RPi.GPIO as GPIO          
from time import sleep

en_L = 22
in1_L = 18
in2_L = 16

en_R = 11
in1_R = 13
in2_R = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(en_L,GPIO.OUT)
GPIO.setup(in1_L,GPIO.OUT)
GPIO.setup(in2_L,GPIO.OUT)
GPIO.setup(en_R,GPIO.OUT)
GPIO.setup(in1_R,GPIO.OUT)
GPIO.setup(in2_R,GPIO.OUT)

GPIO.output(in1_L,GPIO.LOW)
GPIO.output(in2_L,GPIO.LOW)
GPIO.output(in1_R,GPIO.LOW)
GPIO.output(in2_R,GPIO.LOW)

p_L=GPIO.PWM(en_L,1000)
p_R=GPIO.PWM(en_R,1000)

p_L.start(25)
p_R.start(25)

while(1):

    x=input()

    if x=='s':
        print("stop")
        GPIO.output(in1_L,GPIO.LOW)
        GPIO.output(in2_L,GPIO.LOW)

        GPIO.output(in1_R,GPIO.LOW)
        GPIO.output(in2_R,GPIO.LOW)

    elif x=='z':
        print("forward")
        GPIO.output(in1_L,GPIO.HIGH)
        GPIO.output(in2_L,GPIO.LOW)

        GPIO.output(in1_R,GPIO.HIGH)
        GPIO.output(in2_R,GPIO.LOW)

    elif x=='s':
        print("backward")
        GPIO.output(in1_L,GPIO.LOW)
        GPIO.output(in2_L,GPIO.HIGH)

        GPIO.output(in1_R,GPIO.LOW)
        GPIO.output(in2_R,GPIO.HIGH)

    elif x=='l':
        print("low")
        p_L.ChangeDutyCycle(25)
        p_R.ChangeDutyCycle(25)

    elif x=='m':
        print("medium")
        p_L.ChangeDutyCycle(50)
        p_R.ChangeDutyCycle(50)

    elif x=='h':
        print("high")
        p_L.ChangeDutyCycle(75)
        p_R.ChangeDutyCycle(75)


    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")