from app import db, mapped_column, relationship, Integer,  String



class Niveau(db.Model):
    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle  = db.Column(db.String(20), unique=True, nullable=False)
    
    #OneToMany : Niveau---Classe
    classes = db.relationship("Classe", back_populates="niveau")

    #OneToMany : Niveau---Semestre
    semestres = db.relationship("Semestre", back_populates="niveau")


