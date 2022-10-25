from flask import Flask
from router import recognize

app = Flask(__name__)

app.add_url_rule('/recognize', 'recognize', recognize.index, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)