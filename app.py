from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from router import recognize, location
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.add_url_rule('/recognize', 'recognize', recognize.index, methods=["POST"])
app.add_url_rule('/location', 'location', location.index, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)