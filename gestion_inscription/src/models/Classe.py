from app import db, mapped_column,ForeignKey, relationship,Integer,Boolean,String
from .ClasseCours import ClasseCours



class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    libelle = db.Column(db.String(20), unique=True, nullable=False)
    effectif = db.Column(db.Integer)

    #ManyToOne : Classe---Niveau
    niveau_id  = db.Column(db.Integer, db.ForeignKey("niveau.id"))
    niveau = relationship("Niveau", back_populates="classes")

    #ManyToOne : Classe---Filiere
    filiere_id = db.Column(db.Integer, db.ForeignKey("filiere.id"))
    filiere = db.relationship("Filiere", back_populates="classes")

    #OneToMany : Classe---Inscription
    inscriptions = db.relationship("Inscription", back_populates="classe")

    #OneToMany : Classe---Enseignement
    enseignements = db.relationship("Enseignement", back_populates="classe")

    #ManyToMany : Classe---Cours
    cours = db.relationship("Cours", secondary=ClasseCours.__table__, back_populates="classes")
