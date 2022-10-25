import cv2
import os

def index(vidPath):
    video = cv2.VideoCapture(vidPath)
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]

            cv2.imwrite(os.path.join('./imfaces', str(w) + str(h) + '_faces.jpg'), roi_color)
