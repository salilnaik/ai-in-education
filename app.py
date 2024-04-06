from flask import Flask, request
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    # return '<a href="/chat">Chat</a>'
    return render_template('home.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == "POST":
        message = request.form["message"]
        print(message)
    return render_template('index.html')

    
app.run(debug=True)