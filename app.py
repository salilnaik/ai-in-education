from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
            
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text