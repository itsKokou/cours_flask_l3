from flask import Flask,render_template

app = Flask(__name__) #name : nome de là où je suis

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# app.run()
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World!'

# if __name__ == '__main__': #Si on import App.py, l'appli ne sera pas lancée
#     app.run(debug=True)

#? Décorateurs : Callback
# def test():
#     print("Ceci est un test")
#     def test2():
#         print("Ceci est un test2")
#     # test2()
#     return test2

# x = test()
# x() 

# def test(f):
#     print("Ceci est un test")
#     def test2():
#         print("Ceci est un test2")
#     # test2()
#     print(f())
#     return test2 

# x = test(hello)
# x()

# def decorer(f):
#     def Adecorer():
#         print("Avant decoration")
#         f()
#         print("Après decoration")

#     return Adecorer

# @decorer
# def decoration():
#     print("Je suis la decoration")

# decoration()

def getAllProduits():
    return ["mangue","banane","orange","alloco"]

def getProduitByPos(pos:int)->str:
    tab = getAllProduits()
    return tab[pos]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/produits')
def produits():
    p = getAllProduits()
    return render_template("produits.html",produits=p)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/produits/<int:id>')
def produit_id(id):
    # return f"<h1>Produit {id}</h1>"
    p = getProduitByPos(id)
    return render_template("produit.html",produit=p)

app.run(debug=True)