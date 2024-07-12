from app import app, render_template

@app.route("/home")
def hey():
    return render_template("security/login.html")
