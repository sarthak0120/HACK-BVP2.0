##imports
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import dlib
import cv2
import time
import math
from datetime import datetime, date


# Detect Blinks

def eye_aspect_ratio(eye):
  A = dist.euclidean(eye[1], eye[5])
  B = dist.euclidean(eye[2], eye[4])
  
  C = dist.euclidean(eye[0], eye[3])
  ear = (A+B) / (2.0 * C)
  return ear

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", help = "path to facial landmark predictor")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
COUNTER = 0
TOTAL = 0

print("Loading Facial Landmark Predictor....")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS[["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS[["right_eye"]
                                                 
print("Starting Live Video Stream...")
vs = VideoStream(src = 0).start()
fileStream = False
time.sleep(1.0)
currentCount = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                                                  
                                                  
                                                  
                                                  
                                                  
                                            




