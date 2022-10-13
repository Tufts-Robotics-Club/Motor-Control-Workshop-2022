#https://www.digikey.com/en/maker/blogs/2021/how-to-control-servo-motors-with-a-raspberry-pi 
from gpiozero import Servo # Importing Servo library
from time import sleep # Importing sleep 

# Create a servo instance
servo = Servo(25) # Selecting pin 25 to control the servo

try:
    while True: # Always do this
        servo.min() # Put the servo to the min position
        sleep(0.5) # Wait half a second
        servo.mid() # Put the servo to the middle position
        sleep(0.5)
        servo.max() # Put the servo to the max position
        sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")