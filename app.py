from flask import Flask, render_template

app = Flask(__name__)

secrets= "123@22"


@app.route('/')
def home():
    return render_template('index.html')

