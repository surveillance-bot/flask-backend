# Flask API endpoint

### Captures the video on the route "/recognize"
- Accepts a base64 string of the video and decodes it back to a file
- Saves the file to "res.mp4" to compute the recognition algorithm
- Iterates over frames and gets every face in that frame
- For each face detected, iterate over "/imfaces" to find a pre-existing match
- If a match is found, update the location of the face id in the database
- If no match, save this file to the "/imfaces" and insert a row in db

### Returns the location history of a suspect at "/location"
- Expects a base64 string of the face's image and converts it to file
- Saves the file to "res.jpg" in local directory
- Iterates over every file in "/imfaces" and finds for a match
- If a match is found, return the location history of that face id

##### Do not make any changes in /imfaces, it represents every image in the database.