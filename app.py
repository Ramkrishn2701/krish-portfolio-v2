from flask import Flask, render_template, jsonify
from database import load_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  projects = load_db()
  return render_template("home.html", projects=projects, name='krish')


@app.route("/api/jsonify")
def load_projects():
  projects = load_db()
  return jsonify(projects)


app.run(host="0.0.0.0", debug=True)
