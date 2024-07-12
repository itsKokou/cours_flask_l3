from app import db, mapped_column,ForeignKey, relationship,Integer, String,Text


class Declaration(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    motif = db.Column(db.String(100), nullable=False)
    description  = db.Column(db.Text, nullable=True)

    #ManyToOne : Declaration---Seance
    seance_id = db.Column(db.Integer, db.ForeignKey("seance.id"))
    seance = db.relationship("Seance", back_populates="declarations")

    #ManyToOne : Declaration---User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="declarations")
    
    
