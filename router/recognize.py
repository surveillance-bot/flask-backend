from __future__ import print_function
from flask import Flask, jsonify, request, render_template
from scripts import haarcascade
import base64 

def index():
    if request.method == "POST":
        print("Recieved anything?")
    #accept the data from the request
        title = request.form.get('title') 
        location = request.form.get('location') 
        # b64 = request.get_json()["video"]
        # location = request.get_json()["location"]
        print(location,title)
        #convert the base64 video to a file and save it locally
        # video = base64.b64decode(b64)
        # video_result = open('res.mp4', 'wb')
        # video_result.write(video)
        # print("Video is saved in the local")
        
        # #run the face recognition algorithm on the video
        # haarcascade.index("res.mp4", location)
        
    return "Broke the video into frames and saved the faces from each frames."