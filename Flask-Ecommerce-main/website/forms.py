from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, NumberRange
from flask_wtf.file import FileField, FileRequired


class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), length(min=2)])
    password1 = PasswordField('Entrer votre Password', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirmer votre Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Créer')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Entrer votre Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), length(min=6)])
    change_password = SubmitField('Change Password')


class ShopItemsForm(FlaskForm):
    product_name = StringField('Nom du Product', validators=[DataRequired()])
    current_price = FloatField('Prix actuel', validators=[DataRequired()])
    previous_price = FloatField("Prix d'avant", validators=[DataRequired()])
    in_stock = IntegerField('En Stock', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField('Image Produit ', validators=[DataRequired()])
    flash_sale = BooleanField('Vente Flash')

    add_product = SubmitField('Ajouter Produit')
    update_product = SubmitField('Update')


class OrderForm(FlaskForm):
    order_status = SelectField('Statut Commande', choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'),
                                                        ('Out for delivery', 'Out for delivery'),
                                                        ('Delivered', 'Delivered'), ('Canceled', 'Canceled')])

    update = SubmitField('Update Statut')





