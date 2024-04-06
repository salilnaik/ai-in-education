from tkinter import ttk

from flask import Flask, request
from tkinter import *

app = Flask(__name__)
root = Tk()
combo = ttk.Combobox(root)

@app.route("/")
def hello_world():
    return """
            <form method="POST">
                <input name="Major">
                <input name="text">
                <input type="submit">
            </form>"""


@app.route('/', methods=['POST'])
def MajorHandler():
    text = request.form['Major']
    processed_text = text.upper()
    return processed_text