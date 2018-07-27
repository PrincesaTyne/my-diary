from flask import Flask, jsonify, request
import json

app = Flask(__name__)

entries = []

@app.route("/api/v1/entries", methods=["GET"])
def get_all_entries():
    #check if entries list is empty
    if entries == []:
        return jsonify("There are no entries yet"),200
    #get all entries in a list
    else:
        return jsonify(entries),200

@app.route("/api/v1/entries/<string:entryId>", methods=["GET"])
def get_single_entry(entryId):
    #check if entries list is empty
    if entries == []:
        return jsonify("There are no entries yet"),200
    #get a single entry from the entries list
    else:
        for x in entries:
            if x["id"] == entryId:
                return jsonify(x),200

@app.route('/api/v1/entries', methods=['POST'])
def add_entry():
    #get input/ new entry from user 
    entry = request.get_json()
    entry_keys = ["title","content","date","id"]
    for key in entry:
        #check whether the inputed data is valid
        if key not in entry_keys:
            return jsonify("Please enter valid data"),200
        #check whether the id inputed already exists
        elif entry in entries:
            if entry["id"] == entry[key]:
                return jsonify("That id is already taken"),200
        #check whether any field has no content
        elif entry[key] == "":
            return jsonify("One of the fields is empty"),200
    #add the inputed entry to the entries list
    entries.append(entry)
    return jsonify({'Entries': entries}),201

@app.route('/api/v1/entries/<int:entryId>', methods=["PUT"])

def edit_entry(entryId):
    #check if entries list is empty
    if entries == []:
        return jsonify("There are no entries in your diary"),200
    #modify the requested entry
    else:
        for x in entries:
            if x["id"] == entryId:
                x["content"] = request.get_json(entryId)
                x["id"] == x["content"]
    return jsonify ({"your entries": entries}),200
