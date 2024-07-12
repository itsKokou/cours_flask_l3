from app import db, mapped_column, relationship, Integer,Boolean,String


class AnneeScolaire(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived  = db.Column(db.Boolean,default=False, nullable=False)
    isActive = db.Column(db.Boolean, default=False, nullable=False)
    libelle = db.Column(db.String(20),unique=True, nullable=False)

    #OneToMany : AnneeScolaire---Inscription
    inscriptions =  db.relationship("Inscription",back_populates="anneeScolaire")

    #OneToMany : AnneeScolaire---Enseignement
    enseignements = db.relationship("Enseignement", back_populates="anneeScolaire")

    #OneToMany : AnneeScolaire---Cours
    cours = db.relationship("Cours", back_populates="anneeScolaire")

