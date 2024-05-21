from flask import Flask , json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def helloWorld():
    return "Ola mundo!"

@app.route('/users')
def users():
    with open('users.json', 'r') as json_file:
        users = json.load(json_file)
        return users
