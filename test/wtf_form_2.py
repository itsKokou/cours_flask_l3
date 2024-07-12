"""CREATION D'UN FORMULAIRE

1 creer une classe qui herite de FlaskForm ======== pip install -U Flask-WTF
2 Mettre les champs du form
3 Creer une route qui affiche le form
4 Instancier un obj de la classe et l'attacher au template 
"""
from flask import Flask,  render_template
from flask_wtf import FlaskForm #Creer le formulaire
from wtforms import StringField,PasswordField # creer les champs du formulaire


#Classe
class LoginForm(FlaskForm):
    username = StringField("username") 
    password =  PasswordField("password")

app= Flask(__name__)

app.config['SECRET_KEY'] = "voicimaclesecrete"

@app.route('/',methods=['GET', 'POST'])
def index():
    form = LoginForm()
    
    return render_template("wtf_form_2.html",form=form)

if __name__ == "__main__" :
    app.run(debug=True)