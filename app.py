# Import the required packages
from flask import Flask

def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/', methods=["GET"])
def hello():
    return "Hello World"  