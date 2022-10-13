# Motor Workshop Example Code

This repository contains example code for driving motors via both Raspberry Pi and Arduino, as well as reading in a camera feed from a Raspberry Pi.

## Raspberry Pi

The sample code available for Raspberry Pi is as follows:

- `incremental.py`
    - Drives a servo incrementally through its full range of motion
    - Should be run on Raspberry Pi
    - Assumes servo is being controlled over pin 25

- `positions.py`
    - Drives a servo motor to minimum, middle, and max positions
    -  Should be run on Raspberry Pi
    - Assumes servo is rbeing controlled over pin 25

- `read_local_camera_feed.py`
    - Reads and displays, using OpenCV, a video feed from a local PiCamera
    - Should be run on Raspberry Pi

- `read_remote_camera_feed.py`
    - Reads and displays, using OpenCV, a video feed being streamed over TCP
    - Should be run on an external computer, reading a camera feed streamed from a Raspberry Pi
    - Environment variables:
        - `VIDEO_STREAM_ADDRESS` - the IP address over which the video feed is being streamed
        - `VIDEO_STREAM_PORT` - the TCP port over which the video feed is being streamed

- `simpledriving.py`
    - Drives a DC motor at varying speeds and directions
    - Should be run on Raspberry Pi
    - Assumes DC motor being controlled over pins 5 and 12

## Arduino
