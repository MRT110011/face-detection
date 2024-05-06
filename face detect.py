import cv2
import pandas as pd
from datetime import datetime
import time

# Pre-trained Haar cascade model for face-detection is loaded here
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Webcam is initialized
video_capture = cv2.VideoCapture(0)

# DataFrame for storation of the data is initialized
data = {'Time': [], 'Number of Faces': []}
data_frame = pd.DataFrame(data)



# Initialization of the timer , number of faces variable , and time when the cide executes
start_time = time.time()
prev_num_faces = 0
today_date = datetime.now().strftime('%Y_%m_%d_time_%H_%M')

while True:
    # Capturation is done frame-by-frame
    ret, frame = video_capture.read()

    # Captured frame is converted to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Faces are detected in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Number of detected faces are stored
    num_faces = len(faces)

    # Rectangle shape is drawn around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display of number of detected faces on the frame at a given time
    cv2.putText(frame, f'Exit=Q  No. of Faces: {num_faces}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Record the current time and number of faces detected at that time
    if num_faces != prev_num_faces:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_frame.loc[len(data_frame)] = [current_time, num_faces]
        prev_num_faces = num_faces

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check if 3 seconds have elapsed since the last data storage for changes to store
    if time.time() - start_time >= 3:
        # Write the data to an Excel file named '{todayDate}.xlsx'
        data_frame.to_excel(f'{today_date}.xlsx', index=False)
        # Reset of timer
        start_time = time.time()

    # Exit from the loop when button 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
