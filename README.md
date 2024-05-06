Real-Time Face Detection and Counting System

Overview

This project implements a real-time face detection and counting system using Python and OpenCV. It continuously captures video from a webcam, detects faces in the video frames, and counts the number of faces present. The count is then stored in an Excel file along with the timestamp of each count.

Requirements

To run this project, ensure that you have the following dependencies installed:

Python 3.x

OpenCV (opencv-python)

pandas (pandas)

NumPy (numpy)

openpyxl (openpyxl)

You can install these dependencies using pip. Open a terminal or command prompt, navigate to the project directory, and execute the following commands:


pip install opencv-python

pip install pandas

pip install numpy

pip install openpyxl

Usage:

Ensure that your webcam is connected to your computer. Or may be u have a laptop 

download face detect.py and haarcascade...default.xml into your machine .... create a folder and put both file inside that folder and open folder with code editor in which u have set up python then run.

Once the script is running, it will continuously capture video from your webcam and display the live feed with rectangles drawn around detected faces.
The number of faces detected in each frame will be displayed in the top-left corner of the video feed.
The count of faces detected will be recorded along with a timestamp every 3 seconds and stored in an Excel file named YYYY_MM_DD_time_HH_MM.xlsx in the project directory.
Note
Ensure that you have sufficient permissions to write files to the project directory.
Press the 'q' key to stop the script and exit the program
