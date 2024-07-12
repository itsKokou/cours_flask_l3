#Tout ce qui est partagé entre les pages : footer
import os

DEBUG=1

APP_NAME = "KOKOU"

basedir = os.path.abspath(os.path.dirname(__file__))
 
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data.db")

SQLALCHEMY_TRACKMODIFICATIONS = False

SECRET_KEY = "voicimaclesecrete"

NO_IMG = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"

#Pour les pages suivante
USE_SESSION_FOR_NEXT = True

#Remember me time
#REMEMBER_COOK_DURATION = 