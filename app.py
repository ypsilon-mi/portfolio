from flask import Flask, render_template

app = Flask(__name__)
# index = open('index.html').read() - not needed

@app.route('/')
def index():
    return render_template('index.html') 
