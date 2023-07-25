from flask import Flask, request, jsonify, render_template
import os
import csv
from datetime import datetime

app = Flask(__name__, static_url_path='', static_folder='static')

# Your previous get_candidate_odds function
def get_candidate_odds(candidates, directory='.'):
    # ...
    return odds_dict

@app.route('/api/get_candidate_odds', methods=['POST'])
def api_get_candidate_odds():
    candidates = request.json.get('candidates', [])
    directory = "/path/to/your/csv/files"
    result = get_candidate_odds(candidates, directory)
    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

