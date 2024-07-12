from app import db , mapped_column, ForeignKey ,Integer


class ClasseCours(db.Model):
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'), primary_key=True)
    cours_id = db.Column(db.Integer, db.ForeignKey('cours.id'), primary_key=True)
