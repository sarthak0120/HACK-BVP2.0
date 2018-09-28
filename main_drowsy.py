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



