from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import os,sys

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])

def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        
        raise HousingException(e,sys) from e
        logging.info(housing.error_message)
        
        logging.info("we are testing logger module")
        return "first machine learning Project"

if __name__ == "__main__":
    app.run(debug=True)

