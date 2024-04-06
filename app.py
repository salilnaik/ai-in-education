from flask import Flask, request
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

return_message = "test message"

@app.route("/")
def home():
    # return '<a href="/chat">Chat</a>'
    return render_template('home.html')

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