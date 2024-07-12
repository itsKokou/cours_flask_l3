from app import db, mapped_column,ForeignKey, relationship, Integer, String, Boolean


class Semestre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(20), unique=True, nullable=False)
    isActive = db.Column(db.Boolean, default=False, nullable=False)

    
    #OneToMany : Semestre---Cours
    cours = db.relationship("Cours", back_populates="semestre")

    #ManyToOne : Semestre---Niveau
    niveau_id = db.Column(db.Integer, db.ForeignKey("niveau.id"))
    niveau = db.relationship("Niveau", back_populates="semestres")
