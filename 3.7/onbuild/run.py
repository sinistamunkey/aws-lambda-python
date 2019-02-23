import os
from flask import Flask, request, jsonify
from src.lambda_handler import entry_point

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({"status": "ok"})

    if request.method == 'POST':
        response = entry_point(request.json, {})
        return jsonify(response)

app.run(
    debug=True,
    host='0.0.0.0',
    port=os.environ.get('FLASK_PORT', 80),
)
