from flask import Flask, render_template

app = Flask(__name__)

# FAKE TESTING CREDENTIALS TO TRIGGER BETTERLEAKS
# AWS Rules require a 20-character identifier and a 40-character secret key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/')
def home():
    return render_template('index.html')
