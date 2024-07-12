from app import app, request, session,redirect, render_template, create_engine
from ..models.User import User, Role
#---------Login
#login_required protege les route
from flask_login import (LoginManager, UserMixin, login_user , login_required, current_user,logout_user)


#----Config login
login_manager = LoginManager(app)
#Redirige dans login si pas connecté mais veut aller loin
login_manager.login_view = "login"
#Changer le message du please à la redirection vers connexion là
login_manager.login_message = "Veuillez vous connecter !"



#Recupère le user connecté pour le truc de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return redirect("/login")

@app.route('/login', methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        login = request.form["login"]
        password = request.form.get("password")
        #user = User.query.filter_by(login=").first()
        #user = User.query.filter_by(login=login, password=password).first()
        role = Role.query.filter_by(libelle="ROLE_ADMIN")
        print(role)
        user = None
        if not user :
            error="Login ou mot de passe incorrect"
        else:
            # Mettre user dans la session
            login_user(user)

            if 'next' in session :
                next = session["next"]
                if next is not None :
                    return redirect(next)
            else:
                return redirect("/home")
            
            session["next"] = request.args.get("next")
    return render_template("security/login.html", error=error)

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/login")
