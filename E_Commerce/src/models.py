# Rapport avec BD
from flask_sqlalchemy import SQLAlchemy
from .client import app
from flask_migrate import Migrate
# #Creer une instance de la db 
# db = SQLAlchemy()
# #Relier app au db
# db.init_app(app)
# OU 
db= SQLAlchemy(app)
migrate = Migrate(app, db)

class CategorieProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False,  unique=True)
    # Categorie --> Product : ManyToMany
    products = db.relationship('Product', secondary=CategorieProduct.__table__ , back_populates='categories')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False, unique=True)
    description = db.Column(db.Text)
    img_url = db.Column(db.Text)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer, default=0)
    deleted = db.Column(db.Boolean, default=False)
    # Produit --> User : ManyToOne
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='produits')
    # Product --> Categorie : ManyToMany
    categories = db.relationship('Categorie', secondary=CategorieProduct.__table__ , back_populates='products')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20),nullable=False,  unique=True)
    password = db.Column(db.String(100),nullable=False,)
    nom = db.Column(db.String(30),nullable=False)
    prenom = db.Column(db.String(30),nullable=False)
    # User --> Product : OneToMany
    produits = db.relationship('Product', back_populates='user')

with app.app_context():
    db.create_all()

#-------------------- FONCTIONS 

#?--------Produits
    
def getAllProduct():
    #-- SELECT * FROM product
    return Product.query.order_by(Product.title).all()

def saveProduct(p:Product):
    db.session.add(p)
    db.session.commit()

def findProductById(id_product):
    produits = getAllProduct()
    for p in produits:
        if p.id == id_product:
            return p
    return None


#?--------Categorie

def getAllCategorie():
    #-- SELECT * FROM categorie
    return Categorie.query.order_by(Categorie.name).all()

def saveCategorie(c:Categorie):
    db.session.add(c)
    db.session.commit()

def findCategorieById(id_categorie):
    categories = getAllCategorie()
    for c in categories:
        if c.id == id_categorie:
            return c
    return None

#?--------User

def getAllUser():
    #-- SELECT * FROM user
    return User.query.order_by(User.nom).all()

def saveUser(u:User):
    db.session.add(u)
    db.session.commit()

def findUserById(id_user):
    users = getAllUser()
    for u in users:
        if u.id == id_user:
            return u
    return None