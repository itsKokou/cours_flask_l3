from app import db, mapped_column, relationship,Integer, String


class Filiere(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(20), unique=True, nullable=False)
    
    #OneToMany : Filiere---Classe
    classes = db.relationship("Classe", back_populates="filiere")

