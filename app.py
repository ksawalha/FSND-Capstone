from flask import Flask
from flask_cors import CORS
from models import setup_db



app = Flask(__name__)   #setting up the app and database after importing necessary resources
setup_db(app)
CORS(app)

from functions import *  

if __name__ == '__main__':
    app.run(port=8080, debug=True)
