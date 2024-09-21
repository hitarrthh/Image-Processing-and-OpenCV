import streamlit as st
import cv2 as cv
import numpy as np

# Load the Haar Cascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces
def detect_faces(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return frame

# Streamlit app layout
st.title("Face Detection App")

# Start video capture
video_cap = cv.VideoCapture(0)

# Initialize session state for detection status
if 'detection_running' not in st.session_state:
    st.session_state.detection_running = False

# Start detection button
if st.button('Start Detection'):
    st.session_state.detection_running = True
    stframe = st.empty()
    
# Stop detection button
if st.button('Stop Detection'):
    st.session_state.detection_running = False

# Display the video feed while detection is running
if st.session_state.detection_running:
    while True:
        ret, frame = video_cap.read()
        if not ret:
            st.write("Failed to capture video.")
            break
        
        # Detect faces in the frame
        frame = detect_faces(frame)
        
        # Convert frame to RGB for display
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # Show the frame in the app
        stframe.image(frame_rgb, channels='RGB', use_column_width=True)

        # Allow the loop to break when the Stop button is clicked
        if not st.session_state.detection_running:
            st.write("Detection stopped.")
            break

# Release the video capture when done
video_cap.release()

