from flask import Flask, request, redirect, url_for ,session

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello world </h1>"


#---------------- ROUTE PAR DEFAUT

@app.route('/presentation',defaults={"name":"Kokou"})
@app.route('/presentation/<name>')
def presentation(name):
    return "<h1>Hello, je m'appelle {} </h1>".format(name)

#---------------- QUERY PARAM
@app.route('/qs')
def query_string():
    name = request.args
    return "<h1>Hello, je m'appelle</h1>"

#---------------- POST DATA FORM
@app.route('/login')
def login():
    return """
    <form method='POST' action='/connexion'>
        <input type='text' name='username' placeholder='Enter ur username'/>
        <input type='password' name='password' placeholder='Enter ur password'/>
        <button type='submit' name='btn'>Connexion</button>
    </form>
    """
    
@app.route('/connexion', methods=['POST'])
def connexion():
    username = request.form['username']
    pwd = request.form['password']
    return f"CONNECTION SUCCESSFUL: Login = {username} | Password = {pwd}"



#---------------- CREATION DE SESSION
# Il faut les clef secretes pour la session
app.config['SECRET_KEY'] = "voicimaclesecrete"
@app.route('/test')
def test():
    #Insertion
    session['connectedUser'] = "My nigga"
    #Recuperation
    if('connectedUser' in session):
        user = session['connectedUser']

    #Suppression
    session.pop('connectedUser',None)
    pass

if __name__ == "__main__" :
    app.run(debug=True)