# https://www.digikey.com/en/maker/blogs/2021/how-to-control-servo-motors-with-a-raspberry-pi 
from gpiozero import Servo # Importing Servo library
from time import sleep # Importing sleep 

# Create a servo instance
servo = Servo(25) # Selecting pin 25 to control the servo
# Define a variable
val = -1 # Set the variable "val" to value -1

try:
    while True: # Always do this
        servo.value = val # Set the position of the servo to "val"
        sleep(0.1) # Wait for 1/10th of a second
        val = val + 0.1 # Increment "val"
        if val > 1: # If "val" is greated than 1
        	val = -1 # then set "val" back to -1
except KeyboardInterrupt:
	print("Program stopped")