from app import db, mapped_column,ForeignKey, relationship ,Integer,Boolean,Date
from .ClasseCours import ClasseCours

class Cours(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    createAt = db.Column(db.Date, nullable=False)
    nbreHeureTotal = db.Column(db.Integer, default= 0)
    nbreHeureRestantPlan = db.Column(db.Integer, default= 0)
    nbreHeureRealise = db.Column(db.Integer, default= 0)

    #ManyToOne : Cours---AnneeScolaire
    anneeScolaire_id = db.Column(db.Integer, db.ForeignKey("annee_scolaire.id"))
    anneeScolaire = db.relationship("AnneeScolaire", back_populates="cours")

    #ManyToOne : Cours---Semestredb.
    semestre_id = db.Column(db.Integer, db.ForeignKey("semestre.id"))
    semestre = db.relationship("Semestre", back_populates="cours")

    #ManyToOne : Cours---Module
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"))
    module = db.relationship("Module", back_populates="cours")

    #ManyToOne : Cours---Professeur
    professeur_id = db.Column(db.Integer, db.ForeignKey("professeur.id"))
    professeur = db.relationship("Professeur", back_populates="cours")

    #ManyToMany : Cours---Classe
    classes = db.relationship("Classe", secondary=ClasseCours.__table__, back_populates="cours")

    #OneToMany : Cours---Seance
    seances = db.relationship("Seance", back_populates="cours")
   


