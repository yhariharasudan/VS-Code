from flask import Flask, request, jsonify

import json
app = Flask(__name__)
sample = [
    {"name": "a", "role": "intern"}
]
file='result.json'
@app.route('/data', methods=['GET'])
def get_data():
  try:
    return jsonify(sample) , 200
  except Exception as e:
     return jsonify() , 500


@app.route('/data', methods=['POST'])
def add_data():
 try:
    new_data = request.json
    sample.append(new_data)
    with open(file, 'w') as D:
       json.dump(sample,D)
    return jsonify({"message": "Data added successfully", "data": new_data}), 201
 except Exception as e:
     return jsonify({"error":"exception"}) , 500

if __name__ == '__main__':
    app.run(debug=True)
