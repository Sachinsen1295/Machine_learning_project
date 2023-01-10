from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])

def index():
    logging.info("we are testing logger module")
    return "first machine learning Project"

if __name__ == "__main__":
    app.run(debug=True)

