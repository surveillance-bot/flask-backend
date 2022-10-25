from flask import request
import base64 

def index():
    title = request.get_json()["title"]
    b64 = request.get_json()["video"]
    
    video = base64.b64decode(b64)
    video_result = open('res.mp4', 'wb') # create a writable image and write the decoding result
    video_result.write(video)
    
    return "Video conversion is done"
    # return "The video's title is {}".format(title)