from app import db, mapped_column, relationship,Integer, Boolean, String


class Salle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    libelle = db.Column(db.String(20), unique=True, nullable=False)
    nbrePlace = db.Column(db.Integer)

    #OneToMany : Salle---Seance
    seances = db.relationship("Seance", back_populates="salle")


