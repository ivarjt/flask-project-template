#-------------------
# Non Local Imports 
#-------------------
from flask import Flask
#from flask_socketio import SocketIO # pip install flask-socketio
from flask_sqlalchemy import SQLAlchemy


# Global Variables
RUN_IN_DEBUG_MODE = True # Set to False when deploying to production
HOST = "0.0.0.0"

# Flask app config
app = Flask(__name__)

""" Uncomment this section if you want to use SocketIO
# SocketIO 
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
"""

# SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # To reduse some terminal spam, could be turned to True if needed for debugging
db = SQLAlchemy(app)


#---------------------
# Local Imports Below
#---------------------

# Models
from .models import User

# View
from .views import views, other_view