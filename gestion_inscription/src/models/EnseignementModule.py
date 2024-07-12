from app import db, mapped_column, ForeignKey, Integer


class EnseignementModule(db.Model):
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), primary_key=True)
    enseignement_id = db.Column(db.Integer, db.ForeignKey('enseignement.id'), primary_key=True)
    
