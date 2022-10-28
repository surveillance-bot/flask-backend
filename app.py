from flask import Flask,render_template
from router import recognize, location
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return render_template('index.html')

app.add_url_rule('/recognize', 'recognize', recognize.index, methods=["POST"])
app.add_url_rule('/location', 'location', location.index, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)