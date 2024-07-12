# Metier du client
#Au lancement c'est client qui se lance

from flask import Flask,render_template, redirect
# from .fake_data import getAll, findProductById

app = Flask(__name__)

app.config.from_pyfile("../config.py")

from .models import getAllProduct # model a besoin de app

@app.route("/home")
def hello_client():
    produits = getAllProduct()
    return render_template("client/home.html",products=produits)

@app.route('/article/<int:id_product>')
def detail_produit(id_product):
    # produit = findProductById(id_product)
    produit = None
    if  not produit :
        return redirect("/home")
    return render_template("client/product.html",product=produit)