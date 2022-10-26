from flask import request
from deepface import DeepFace

def index():
    b64 = request.get_json("image")
    #convert the base64 to a file and save to local dir
    image = base64.b64decode(b64)
    image_result = open('res.jpg', 'wb')
    image_result.write(image)
    #find if any face matches this face
    try:
        is_a_face = DeepFace.detectFace("res.jpg") 
        # find if this face matches something in the database
        for imface in os.scandir('./imfaces'):
            try:
                result = DeepFace.verify(img1_path = imface.path, img2_path = "res.jpg")
                if result["verified"] == True:
                    # return the database location of imface.path file
                    return "The face id of this person is: {}".format(imface.path)
                    break
            except:
                print("No face detected in this image")

    except:
        return "This face is not a face"