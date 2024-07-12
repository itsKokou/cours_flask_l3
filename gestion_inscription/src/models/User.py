from app import db, mapped_column,ForeignKey, relationship, Integer, String, Boolean, Text, Mapped
from flask_login import UserMixin



class User(UserMixin,db.Model):

    id = db.Column(db.Integer ,primary_key=True, autoincrement=True)
    isArchived = db.Column(db.Boolean, default=False, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nomComplet = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)

    # #OneToMany
    declarations = db.relationship("Declaration", back_populates="user")

    #ManyToOne : User---Role
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role =  db.relationship("Role", back_populates="users")

    #Joined Table Inheritance
    __mapper_args__ = {
        "polymorphic_identity": "employee",
        "polymorphic_on": "type",
    }



class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(20), unique=True, nullable=False)

    #OneToMany : Role---User
    users = db.relationship("User", back_populates="role")

