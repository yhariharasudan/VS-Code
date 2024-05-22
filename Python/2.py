from flask import Flask, request, jsonify 
import os
app = Flask(__name__)
@app.route('/write-to-file', methods=['POST'])
def write_to_file():
    try:
        # Get the data from the POST request
        data = request.json
        # Define the file path (you can change this to whatever path you prefer)
        file_path = 'output.txt'
        # Write the data to the file
        with open(file_path, 'w') as f:
            f.write(str(data))
        return jsonify({"message": "Data written to file successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)