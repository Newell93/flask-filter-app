from flask import Flask, render_template, request
#from foo import XXX
app = Flask(__name__)

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/result")
def results():