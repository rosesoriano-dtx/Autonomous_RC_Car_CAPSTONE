import Jetson.GPIO as GPIO
import time

# Set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN) #Enable A
GPIO.setup(15, GPIO.IN) #Enable B
GPIO.setup(19, GPIO.IN) #In1
GPIO.setup(31, GPIO.IN) #In2
GPIO.setup(33, GPIO.IN) #In3
GPIO.setup(35, GPIO.IN) #In4

# Control one motor to go forward
GPIO.output(19, True)   # All the IN's
GPIO.output(31, False)
GPIO.output(33, False)
GPIO.output(35, False)

GPIO.output(13, True)
print("on")