from flask import Flask, request ,jsonify
import os
app =Flask(__name__)

@app.route("/get-user/<user_id>")

def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "hari",
        "role":"intern"
    }
    extra =request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data),201

@app.route("/create-data",methods=["POST"])
def create_data():
   try:
    data= request.json

    newfile='result.txt'
    with open(newfile,'w') as f:
        f.write(str(data))
    return jsonify({"message":"data returend"}),201
   except Exception as e:
    return jsonify({"error":"str(e)"}),500
   





@app.route("/value")
def data():
    data={

    }
    return jsonify(data),200
if __name__ == "__main__":
    app.run(debug=True)