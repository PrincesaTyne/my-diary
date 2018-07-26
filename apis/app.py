from flask import Flask, jsonify, request
import json

entries = []

@app.route("/api/v1/entries", methods=["GET"])
def get_all_entries():
    return jsonify(entries),200

@app.route("/api/v1/entries/<string:entryId>", methods=["GET"])
def get_single_entry(entryId):
    for x in entries:
        if x["id"] == entryId:
            return jsonify(x)
        else:
            return jsonify("That entry does not exist")

@app.route('/api/v1/entries', methods=['POST'])
def add_entry():
    entry = request.get_json()
    entry_keys = ["title","content","date","id"]
    for key in entry:
        if key not in entry_keys:
            return jsonify("Please enter valid data")
        #elif (entry["id"] == entry[key]):
            #return jsonify("That id is already taken")
        elif (len(entry.keys()) != 4):
            return jsonify("Some info is missing")
    entries.append(entry)
    return jsonify({'Entries': entries})

@app.route('/api/v1/entries/<int:entryId>', methods=["PUT"])
def edit_entry(entryId):
    if entries == []:
        return jsonify("There are no entries in your diary")
    else:
        for x in entries:
            if x["id"] == entryId:
                    x["content"] = request.get_json(entryId)
    return jsonify ({"your entries": entries})



if __name__ == "__main__":
    app.run(debug= True, port=3000)