from flask import Flask, render_template
import requests
from utils import primes
app = Flask(__name__)

@app.route("/")
def home():
    ps = primes(1000)
    return render_template("home.html.j2", primes=ps)

@app.route("/about")
def about():
    return render_template("about.html.j2")

if __name__ == '__main__':
    app.run(debug=True)