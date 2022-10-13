from gpiozero import PhaseEnableMotor # Importing the PhaseEnableMotor
from time import sleep # Importing sleep 

#motor = PhaseEnableMotor(phase[direction], enable[PWM])
# The enable pin indicates how fast the motor will drive
# The phase pin indicates which direction the motor will drive (forward or reverse)
motor = PhaseEnableMotor(5, 12) # Selecting which pins to control the DC motor

##########################
# Testing out the motor 
motor.forward(0.5) # Sets the pins to drive the motor forward at half speed
sleep(2)
motor.backward(0.5)
sleep(2)
motor.forward() # Default value = 1
sleep(2)
motor.reverse() # Reverses the direction of the motor, maintains speed
sleep(2)
motor.stop() # Stops the motor


##########################
# Driving faster and fater 
val = 0 # Set the variable "val" to value 0
while True: # Always do this
    val = val + 0.05 # Increase val by 0.05
    motor.forward(val) # Drive motor forward at speed "val"
    sleep(0.25) # Sleep for 1/4th of a second
    if val >= 0.5: # If val is >= 0.5
        break # Break out of the while loop (end the program)
    