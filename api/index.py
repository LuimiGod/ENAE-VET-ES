"""Debug temporal: muestra el path que Flask recibe desde Vercel."""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({
        "path": request.path,
        "full_path": request.full_path,
        "script_name": request.environ.get("SCRIPT_NAME", ""),
    }), 200
