from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from router import recognize, location
from flask_cors import CORS
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('video_face_reco.html')


app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

app.add_url_rule('/recognize', 'recognize', recognize.index, methods=["POST"])
app.add_url_rule('/location', 'location', location.index, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)