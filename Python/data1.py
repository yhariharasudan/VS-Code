from flask import Flask, request,jsonify
import os
import json
app=Flask(__name__)

file='result.json'

def load_data():
    if os.path.exists(file):
        with open(file,'r') as f:
            return json.load(f)
    else:
        return[]
def save(data):
    with open(file,'w') as n:
        json.dump(data,n)

@app.route('/',methods=['GET'])
def get_data():
    try:
        data=load_data()
        return jsonify(data),200
    except Exception as e:
        return jsonify() ,500
    

@app.route('/data',methods=['POST'])   
def add_data():
 try:
    new=request.json
    data=load_data()
    data.append(new)
    save(data)
    return jsonify({"message":"Data Added"}) ,201
 except Exception as e:
     return jsonify({"error":"error occured"}),500
 
@app.route('/data/<int:index>', methods=['PUT'])
def update_data(index):
    try:
        update = request.json
        data = load_data()
        if  0 <= index < len(data):
            data[index] = update
            save(data)  # Save the updated data to the file
            return jsonify({"message": "Data updated successfully", "data": update}), 200
        else:
            return jsonify({"error": "Index not found"}), 404
    except Exception as e:
        return jsonify({"error": "exception"}), 500
    
@app.route('/data/<int:index>', methods=['DELETE'])
def delete_data(index):
    try:
        data=load_data()
        if 0<= index <len(data):
            del data[index]
            save(data)
            return jsonify({"message": f"Data for key '{index}' deleted successfully"}), 200
        else:
            return jsonify({"error": "ID not found"}), 404
    except Exception as e:
        return jsonify({"error": "error occured"}), 500

@app.route('/hello/<int:index>', methods=['GET'])
def hello_data(index):
    try:
        data = load_data()
        if  0 <= index < len(data):
            name = data[index]["name"]
        else:
            name = "world"

        return jsonify({"message": f"Hello {name}"}), 200
    except Exception as e:
        return jsonify({"error": "exception"}), 500

if __name__ == '__main__':
    app.run(debug=True,port=2000,host='0.0.0.0')