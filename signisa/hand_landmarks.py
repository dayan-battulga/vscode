import mediapipe as mp
import cv2
import os
from matplotlib import pyplot as plt
import time
import numpy as np


### Get the mediapipe solution/model
mp_holistic = mp.solutions.holistic # Holistic model in use
mp_drawing = mp.solutions.drawing_utils # Utilities used to draw the landmarks


def mediapipe_detection(image, model):
    # CV reads frames in BGR and Mediapipe detects based on RGB
    # Must convert so Mediapipe can detect it
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False        # IMAGE CANNOT BE EDITTED
    results = model.process(image)      # PREDICTION OF GESTURE FROM MODEL
    image.flags.writeable = True        # IMAGE CAN BE EDITTED 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

### Open camera to get the video feed
cap = cv2.VideoCapture(0)  # 0 for the default camera

# Use the Holistic Model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Reads the frame (ret -> boolean value if frame is read, frame -> an array vector containing the values of the frame)
        ret, frame = cap.read()

        image, results = mediapipe_detection(frame, holistic)
        print(results.right_hand_landmarks)

        # Shows the screen
        cv2.imshow('CV Camera', frame)

        # Close the video feedback if 'q' is pressed
        if (cv2.waitKey(9) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()

plt.imshow(frame)