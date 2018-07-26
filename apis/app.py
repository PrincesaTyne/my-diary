from flask import Flask, jsonify, request
import json

app = Flask(__name__)

entries = []

@app.route("/api/v1/entries", methods=["GET"])
def get_all_entries():
    return jsonify(entries)

@app.route("/api/v1/entries/<string:entryId>", methods=["GET"])
def get_single_entry(entryId):
    
    for x in entries:
        if x.keys() == entryId:
            return x
    return jsonify(x)

@app.route('/api/v1/entries', methods=['POST'])
def add_entry():
    entry = request.get_json()
    entry_keys = ["title","content","date","id"]
    for key in entry:
        if (key not in entry_keys) and (len(entry) != 4):
            return jsonify("Please enter valid data")
    entries.append(entry)
    return jsonify({'Entries': entries})

@app.route('/api/v1/entries/<string:entryId>', methods=["PUT"])
def edit_entry(entryId):
    for i in range(0,3):
        entry_dict = {
                    "id": 1,
                    "title": "content",
                    "date": "1/1/1800",
                    "time": "2:00pm"}
        entries.append(entry_dict)
        entry_dict["id"] +=1
    for x in entries:
        for a,b in x:
            if a == entryId:
                b = request.get_json(entryId)
    return jsonify ({"your entries": entries})

@app.route('/api/v1/entries/<string:entryId>', methods=["DELETE"])
def remove_entry(entryId):
    for x in entries:
        for a in x.keys():
            if a== entryId:
                entries.remove(x)
    return jsonify({"Your entries": entries})

if __name__ == "__main__":
    app.run(debug= True, port=3000)