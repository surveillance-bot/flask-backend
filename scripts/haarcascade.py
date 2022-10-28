import cv2
import os
from deepface import DeepFace
import random 
import matplotlib.pyplot as plt
import uuid
from datetime import date, datetime


def index(vidPath, location):
    count = 0 # 1 frame per second
    jump = 0
    p = 100 #padding
    
    video = cv2.VideoCapture(vidPath)
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()
        if ret == False:
            break
        
        count += 10 
        jump += 1
        video.set(cv2.CAP_PROP_POS_FRAMES, count)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=2,
            minNeighbors=3,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x - p, y - p), (x + w + p, y + h + p), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]
            cv2.imwrite('temp.jpg', roi_color)
            
            try:
                is_a_face = DeepFace.detectFace("temp.jpg") 
                found_a_match = False
                matched_path = ""

                # find if this face matches something in the database
                for imface in os.scandir('./imfaces'):
                    if imface.is_file():
                        #deepface verify the face
                        try:
                            result = DeepFace.verify(img1_path = imface.path, img2_path = "temp.jpg")
                            if result["verified"] == True:
                                found_a_match = True
                                matched_path = imface.name

                        except:
                            print("No face detected in this image")
                
                
                if found_a_match == False:   
                    # database mein create a new row with uuid and location
                    uniqueid = uuid.uuid1()
                    file_name = str(uniqueid) + '.jpg'
                    cv2.imwrite(os.path.join('./imfaces', file_name), roi_color)
                    print("Saving a new image with the id: ", uniqueid)
                else:
                    print("The matched face of this face is of path: ", matched_path)
                    
            except:
                print("This face is not a face")
