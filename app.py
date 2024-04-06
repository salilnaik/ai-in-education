from flask import Flask, request, redirect, render_template
from chatgpt import Chat

app = Flask(__name__, static_url_path='/static')

chat = Chat()
return_message = "Welcome to the career companion. Do you have any questions?"

@app.route("/")
def home():
    # return '<a href="/chat">Chat</a>'
    return render_template('home.html')

@app.route("/submit", methods=['POST'])
def submit():
    return redirect("/chat")

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    global return_message
    if request.method == "POST":
        message = request.form["message"]
        return_message = message
    return render_template('index.html')

@app.route('/message', methods=['GET'])
def message():
    return return_message
    
app.run(debug=True)