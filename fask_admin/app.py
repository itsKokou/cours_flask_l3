from flask import Flask 
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy 
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate


app =  Flask(__name__)
app.config.from_pyfile("./config.py")
app.app_context().push()

db = SQLAlchemy(app)

migrate = Migrate(app,db)

admin = Admin(app,template_mode="bootstrap3")
#Model 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    sexe = db.Column(db.Enum("Masculin","Feminin"), default="Feminin")
    birthday = db.Column(db.Date)
    articles = db.relationship("Article", back_populates="user")

    def __repr__(self) -> str:
        return f"{self.firstname} {self.lastname}"

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="articles")
    #user = db.relationship("User", backref="articles")


class ArticleView(ModelView):
    form_columns=["title","description","user"]

#Ajouter un modelView
admin.add_view(ModelView(User,db.session))
admin.add_view(ArticleView(Article,db.session))

db.create_all()

if __name__ == "__main__":
    app.run()