from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/json')
def get_json_response():
    return jsonify(
        username="admin",
        password="admin",
        role="admin"
    )

if __name__ == "__main__":
    app.run();