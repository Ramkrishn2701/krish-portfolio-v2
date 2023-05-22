from flask import Flask, render_template

app = Flask(__name__)
name = 'krish'


@app.route("/")
def hello_world():
  return render_template("home.html")


app.run(host="0.0.0.0", debug=True)
