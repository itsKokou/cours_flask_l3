from app import db, mapped_column,ForeignKey, relationship,Integer, String, Boolean, Date, Time



class Seance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    isAbsence = db.Column(db.Boolean, default=False, nullable=False)
    codeSeance = db.Column(db.String(20), nullable=True)
    date = db.Column(db.Date, nullable=False)
    heureD = db.Column(db.Time, nullable=False) 
    heureF = db.Column(db.Time, nullable=False)

    #ManyToOne : Seance---Cours
    cours_id = db.Column(db.Integer, db.ForeignKey("cours.id"))
    cours = db.relationship(db.Integer, back_populates="seances")

    #ManyToOne : Seance---Salle : Optional
    salle_id = db.Column(db.Integer, db.ForeignKey("salle.id"), nullable=True)
    salle = db.relationship("Salle", back_populates="seances")

    #OneToMany : Seance---Absence
    absences = db.relationship("Absence", back_populates="seance")

    #ManyToOne : Seance---Professeur
    professeur_id = db.Column(db.Integer, db.ForeignKey("professeur.id"), nullable=True)
    professeur = db.relationship("Professeur", back_populates="seances")

    # #OneToMany : Seance---Declaration
    declarations = db.relationship("Declaration", back_populates="seance")


   
   


