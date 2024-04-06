from flask import Flask, request
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return '<a href="/chat">Chat</a>'

@app.route("/chat")
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def MajorHandler():
    text = request.form['Major']
    processed_text = text.upper()
    return processed_text