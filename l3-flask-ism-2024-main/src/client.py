from flask import Flask, render_template, redirect,url_for
# from .fake_data import getAll,findProductById


app = Flask(__name__)

app.config.from_pyfile("../config.py")

from .models import getAll 
@app.route("/home")
def home_c():
    prods = getAll()
    print(prods)
    return render_template("client/home.html",products=prods)

@app.route("/products/<int:id_product>")
def detail_prod_c(id_product):
    # prod = findProductById(id_product)
    prod = None
    if not prod:
        return redirect(url_for("home_c"))
    return render_template("client/product.html",product=prod)