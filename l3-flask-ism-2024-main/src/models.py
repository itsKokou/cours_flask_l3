from flask_sqlalchemy import SQLAlchemy
from .client import app


# # Creer une instance de la base
# db = SQLAlchemy()
# # Relier l'application avec la base de donnee
# db.init_app(app)
# ou bien
db = SQLAlchemy(app)


# CREATIONS DES MODELES

class Product(db.Model):
    # __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)
    img_url = db.Column(db.Text)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer, default=0)
    deleted = db.Column(db.Boolean,default=False)


with app.app_context():
    # db.drop_all()
    db.create_all()
# =============LES FONCTIONS POUR LA TABLE PRODUIT

def getAll():
    # return "SELECT * FROM product"
    return Product.query.order_by(Product.title).all()

def saveProduct(p: Product):
    db.session.add(p)
    db.session.commit()
    