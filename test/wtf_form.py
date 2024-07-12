"""INSTALLATION DE WTF

1 Installation ======== pip install -U Flask-WTF
2 Importation ======== from flask_wtf import FlaskForm
3 Avoir une clé secrete 
"""
from flask import Flask,  render_template
from flask_wtf import FlaskForm #Creer le formulaire
from wtforms import StringField,PasswordField # creer les champs du formulaire

app= Flask(__name__)

app.config['SECRET_KEY'] = "voicimaclesecrete"
