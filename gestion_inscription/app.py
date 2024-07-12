from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Integer, String, Double, Date, Time, Text, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped , relationship
from flask_migrate import Migrate

app = Flask(__name__,template_folder="src/templates",static_folder="src/static")

app.config.from_pyfile("config/config.py")
app.app_context().push()

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app)
migrate = Migrate(app,db)


from src.controllers import *
from src.models import *




#------------ CONNEXION ---------------------

from flask_login import (LoginManager, UserMixin, login_user , login_required, current_user,logout_user)

@app.route("/home")
@login_required
def home():
    return render_template("layouts/base.html")






