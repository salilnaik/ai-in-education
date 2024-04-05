from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
            <form method="POST">
                <input name="text">
                <input name="text">
                <input type="submit">
            </form>"""
            
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text