from app import db, mapped_column,ForeignKey, relationship,Integer
from .EnseignementModule import EnseignementModule


class Enseignement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    #ManyToOne : Enseignement---AnneeScolaire
    anneeScolaire_id = db.Column(db.Integer, db.ForeignKey("annee_scolaire.id"))
    anneeScolaire = db.relationship("AnneeScolaire", back_populates="enseignements")

    #ManyToOne : Enseignement---Professeur
    professeur_id = db.Column(db.Integer, db.ForeignKey("professeur.id"))
    professeur = db.relationship("Professeur", back_populates="enseignements")

    #ManyToMany : Enseignement---Classe
    classe_id = db.Column(db.Integer, db.ForeignKey("classe.id"))
    classe = db.relationship("Classe", back_populates="enseignements")

    #ManyToMany : Enseignement---Module
    modules = db.relationship("Module", secondary=EnseignementModule.__table__, back_populates="enseignements")

