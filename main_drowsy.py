##imports
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import dlib
import cv2

# Detect Blinks

def eye_aspect_ratio(eye):
  A = dist.euclidean(eye[1], eye[5])
  B = dist.euclidean(eye[2], eye[4])
  
  C = dist.euclidean(eye[0], eye[3])
  ear = (A+B) / (2.0 * C)
  return ear

# Get CMD Command

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", help = "path to facial landmark predictor")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
COUNTER = 0
TOTAL = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS[["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS[["right_eye"]
                                                 
vs = VideoStream(src = 0).start()
currentCount = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  frame = vs.read()
  frame = imutils.resize(frame, width=450)
  height, width, c = frame.shape

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  face = face_cascade.detectMultiScale(gray, 1.15)

  min_dis = 100000
  x=0
  y=0
  w=0
  h=0
  for (mx, my, mw, mh) in face:
    d = dist.euclidean((mx+w/2, my+h/2), (width/2, height/2))
    if(d < min_dis):
      min_dis = d
      x = mx
      y = my
      w = mw
      h = mh

  # detect faces in the grayscale frame
  rects = detector(gray, 0)
  prevcount = 0
  # loop over the face detections
  for rect in rects:
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    # extract the left and right eye coordinates, then use the
    # coordinates to compute the eye aspect ratio for both eyes
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    danger = 0
    # average the eye aspect ratio together for both eyes\ 
    ear = (leftEAR + rightEAR) / 2.0
    leftEyeHull = cv2.convexHull(leftEye)
    rightEyeHull = cv2.convexHull(rightEye)
    cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
    cv2.drawContours(frame, [rightEyeHull],  -1, (0, 255, 0), 1)
                                                  
    if (leftEAR < EYE_AR_THRESH - 0.12 and rightEAR < EYE_AR_THRESH - 0.12):
      print("Both Eyes Blinked")
      continuous_counter = continuous_counter + 1
      if(continuous_counter>7):
        danger = 1
      COUNTER += 1
      TOTAL += 1    
      prevcount = COUNTER
            
    else:
      continuous_counter = 0
    
    cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "Left: {:.2f}".format(leftEAR), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "Right: {:.2f}".format(rightEAR), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, "DANGER!!: {:.2f}".format(danger), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    break

  cv2.imshow("Frame", frame)
  key = cv2.waitKey(1) & 0xFF

  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break

cv2.destroyAllWindows()
vs.stop()
                                                 
                                                  
                                                  
                                            




