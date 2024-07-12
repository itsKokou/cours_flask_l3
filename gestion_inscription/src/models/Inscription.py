from app import db, mapped_column,ForeignKey, relationship, Integer, Boolean, Date


class Inscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    createAt = db.Column(db.Date, nullable=False)

    #ManyToOne : Inscription---AnneeScolaire
    anneeScolaire_id = db.Column(db.Integer, db.ForeignKey("annee_scolaire.id"))
    anneeScolaire = db.relationship("AnneeScolaire", back_populates="inscriptions")

    #ManyToOne : Inscription---Classe
    classe_id = db.Column(db.Integer, db.ForeignKey("classe.id"))
    classe = db.relationship("Classe", back_populates="inscriptions")

    #ManyToOne : Inscription---Etudiant
    etudiant_id = db.Column(db.Integer, db.ForeignKey("etudiant.id"))
    etudiant = db.relationship("Etudiant", back_populates="inscriptions")

     
   


