from flask import Flask, session,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#---------Login
#login_required protege les route
from flask_login import (LoginManager, UserMixin, login_user , login_required, current_user,logout_user)


app = Flask(__name__)

app.config.from_pyfile("./config.py")
app.app_context().push() # Même chose que with app.app_context()

#----Config login
login_manager = LoginManager(app)
#Redirige dans login si pas connecté mais veut aller loin
login_manager.login_view = "login"
#Changer le message du please à la redirection vers connexion là
login_manager.login_message = "Veuillez vous connecter !"

db = SQLAlchemy(app)
migrate = Migrate(app,db)


class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer, default=13)

#Recupère le user connecté pour le truc de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return "<h1>Index!</h1>"

@app.route('/login', methods=["GET", "POST"])
def login():
    # user = User.query.filter_by(login="kokou").first()
    # Mettre user dans la session
    # login_user(user)
    # return "<h1>Vous vous êtes connecté !</h1>"
    if request.method == "POST":
        login = request.form["login"]
        user = User.query.filter_by(login=login).first()
        if not user :
            return "<h1>Va créer un compte !</h1>"
        #TODO: Pour remember me == login_user(user,remember=True)
        login_user(user)
        
        if 'next' in session :
            next = session["next"]
            if next is not None :
                return redirect(next)
            print(next)
        #return "<h1>Vous vous êtes connecté !</h1>"
        session["next"] = request.args.get("next")
    return render_template("login.html")

@app.route('/home')
@login_required
def home():
    return "<h1>Welcome home {} !</h1>".format(current_user.login)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)

@app.route('/logout')
def logout():
    logout_user()
    return "<h1>Vous êtes déconnecté !</h1>"

if __name__=="__main__":
    app.run()