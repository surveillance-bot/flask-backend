from flask import request
from deepface import DeepFace
import base64 
import os 
from reportlab.pdfgen import canvas
import cv2
import matplotlib.pyplot as plt
import subprocess

def create_report(id_new):
    pdf_file = 'suspect.pdf' 
    print("id_new", id_new)
    can = canvas.Canvas(pdf_file)
    if id_new:    
        img_file = "C:/Users/daksh/Desktop/VSCode/SurveillanceBot/flask-backend/imfaces/" + id_new + '.jpg'
        can.drawImage(img_file, 20, 600, width=100)
        can.drawString(20, 450, "The suspect was present at timestamps 5, 6, 6, 6 and 7")
    else:
        can.drawString(20, 700, "No matching face found in database.")
        
    can.save()
    subprocess.Popen(['suspect.pdf'],shell=True)


def index():
    # b64 = request.get_json()["image"]
    #convert the base64 to a file and save to local dir
    # image = base64.b64decode(b64)
    # image_result = open('res.jpg', 'wb')
    # image_result.write(image)
    #find if any face matches this face
    id_find = None 
    
    try:
        is_a_face = DeepFace.detectFace("final.jpg")
        # find if this face matches something in the database
        for imface in os.scandir('./imfaces'):
            print(imface.path)
            
            try:
                result = DeepFace.verify(img1_path = imface.path, img2_path = "final.jpg")

                if result["verified"] == True:
                    # return the database location of imface.path file
                    id_find = (imface.name.split(".")[0])
                    print("VErified a face")
            except:
                print("No face detected in this image")
        
        create_report(id_find)
        return "Report generated."
    except:
        return "This face is not a face"
    