from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder="src/templates")

@app.route('/')
def home():
    return render_template("admin/home.html")

if __name__ == "__main__":
    app.run(debug=True)