#Tout ce qui est partagé entre les pages : footer
import os

DEBUG=1

APP_NAME = "KOKOU"

basedir = os.path.abspath(os.path.dirname(__file__))
 
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"boutique.sqlite")

SQLALCHEMY_TRACKMODIFICATIONS = False

SECRET_KEY = "voicimaclesecrete"

NO_IMG = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"
