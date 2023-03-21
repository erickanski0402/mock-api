from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Server works!"

@app.route('/v3/store')
def store():
    return "Boo 500 on store!", 500

@app.route('/v3/search')
def search():
    return "Boo 500 on search!", 500
