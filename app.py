from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html",
                         name='Siva Rama Krishnan',
                         position='Frontend Developer',
                         type='fresher')


app.run(host="0.0.0.0", debug=True)
