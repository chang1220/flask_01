from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/t/<t>")
def getTemp(t):
    return f"Temperature,{escape(t)}!"

app.route("/h/<h>")
def getHumidity(h):
    return f"Humidity,{escape(h)}!"

@app.route("/th")
def getTempHumidity():
    args = request.args
    return f'Temperature:{escape}'

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}  你好帥!"