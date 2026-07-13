from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')

def hello_world():
  return render_template("index.html")

@app.route('/bye')
def bye():
  return "Bye!!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
  return f"Hello there {name}, r u {number} year old!!!!!!"


if __name__=="main":
  app.run(debug=True)