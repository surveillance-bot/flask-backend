import cv2
import os
from deepface import DeepFace
import random 
import matplotlib.pyplot as plt
import uuid

def index(vidPath, location):
    video = cv2.VideoCapture(vidPath)
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=2,
            minNeighbors=3,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
                        print(imface.path)
                        try:
                            result = DeepFace.verify(img1_path = imface.path, img2_path = "temp.jpg")
                            print(result)
                            if result["verified"] == True:
                                print("found a match")
                                found_a_match = True
                                matched_path = imface.name
                                
                        except:
                            print("No face detected in this image")
                
                
                if found_a_match == False:   
                    uniqueid = uuid.uuid1()
                    file_name = str(uniqueid) + '.jpg'
                    cv2.imwrite(os.path.join('./imfaces', file_name), roi_color)
                    # database mein create a new row with uuid and location
                    
                # else:
                    # insert the "location" of cctv in the matched_path
            except:
                print("This face is not a face")
