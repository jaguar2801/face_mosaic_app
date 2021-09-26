import mediapipe
import cv2 
import numpy 
import mediapipe as mp
from . mediapipe_new.mediapipe.python.solutions import drawing_utils 
import math
import matplotlib.pyplot as plt
import sys

def face_mozaic(img_url,output_url):
    input_img=img_url
    image=cv2.imread(input_img)

    mp_drawing = drawing_utils 
    mp_face_detection = mp.solutions.face_detection

    face_detection=mp_face_detection.FaceDetection(min_detection_confidence=0.2, model_selection=1) 

    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    DESIRED_HEIGHT = 480
    DESIRED_WIDTH = 480
    def resize_and_show(image):
        h,w = image.shape[:2]
        if h < w:
            img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
        else:
            img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
            
        return img  
        
    annotated_image = image.copy()
    for detection in results.detections:
        annotated_image=mp_drawing.draw_detection(annotated_image, detection)
        debug_image=resize_and_show(annotated_image)
    #import pdb; pdb.set_trace()    


    cv2.imwrite(output_url,debug_image)
    print('output image saved to ', output_url)


