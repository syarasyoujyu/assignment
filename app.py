from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "SWE-agent is running!"

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        data = request.json
    else:
        data = {"sample_key": "sample_value"}  # GETリクエストの場合のサンプルデータ

    output_file = os.path.join('data', 'output.txt')
    with open(output_file, 'w') as f:
        f.write(str(data))

    return jsonify({"message": "File generated", "file": output_file})

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


