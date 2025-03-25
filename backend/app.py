from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to My Simple Flask App!"})

if __name__ == '__main__':
    app.run(debug=True)