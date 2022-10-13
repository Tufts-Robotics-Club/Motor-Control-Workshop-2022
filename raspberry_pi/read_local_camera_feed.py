# NAME: read_local_camera_feed.py
# PURPOSE: reading and displaying (using OpenCV) a video feed from a local 
#          camera on a Raspberry Pi
# AUTHOR: Emma Bethel

import cv2

from picamera import PiCamera
from picamera.array import PiRGBArray

# set up/connect to camera
camera = PiCamera()
raw_capture = PiRGBArray(camera)

try:
    while True:
        # get and store the most recent frame from the image
        camera.capture(raw_capture, format='bgr')
        frame = raw_capture.array

        # display video feed
        cv2.imshow("Video Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
	print("Program stopped")
        
