"""   BASE DE DONNEES : INSTALLATION - CONFIGURATION - REQUÊTES DE BASE

pip install Flask-SQLAlchemy
"""

import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configuration de SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Disable les msg du db
basedir = os.path.abspath(os.path.dirname(__file__)) #le chemin absolu de ce fichier ci
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"db.sqlite")



#Initialiser la bd
db = SQLAlchemy(app)


# Classe à mapper à la bd
class User(db.Model):
    #__tablename__ = "users" == changer nom de la table
    #Ajout de column 
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    age = db.Column(db.Integer)

    #Creer le constructeur
    def __init__(self,nom,prenom,age) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age

    #La methode ToString (console)
    def __repr__(self) -> str:
        return (
            f"User : {self.nom} - {self.prenom} - {self.age} "
        )

#Spécifier le contexte pour pouvoir créer
with app.app_context():
    db.create_all()

    #Requete d'insertion obj : ORM
    kokou = User("Kokou","Godwin",20)
    print(kokou.id)
    db.session.add(kokou) # Ajouter dans le tampon 
    print(kokou.id)
    db.session.commit() #Pour enregistrer dans la base
    print(kokou.id)


if __name__ == "__main__":
    app.run(debug=True)