from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>ENAE VET — OK</h1>"


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200
