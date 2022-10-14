# NAME: read_remote_camera_feed.py
# PURPOSE: reading and displaying (using OpenCV) a video feed being streamed
#          over TCP
# AUTHOR: Emma Bethel

import os
import cv2


# get IP address and port of video stream from environment variables
ADDRESS = os.environ.get("VIDEO_STREAM_ADDRESS","localhost")
PORT = os.environ.get("VIDEO_STREAM_PORT", "9000")

# connect to video stream
stream = cv2.VideoCapture(f"tcp://{ADDRESS}:{PORT}")

try:
    while True:
        # get and store the most recent frame from the image
        _, frame = stream.read()

        # display video feed
        cv2.imshow("Video Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
	print("Program stopped")
