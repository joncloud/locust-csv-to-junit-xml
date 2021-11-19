from flask import Flask

app = Flask(__name__)

@app.route("/")
def ok():
    return "1"

@app.route("/fail")
def not_found():
  return "0", 404
