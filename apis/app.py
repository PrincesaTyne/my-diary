from flask import Flask, jsonify, request
import json

app = Flask(__name__)

entries = []

@app.route("/api/v1/entries", methods=["GET"])
def get_all_entries():
    """ Retrieve all entries from the list of entries"""
    if entries == []:
        return jsonify("There are no entries yet"),200
    else:
        return jsonify(entries),200

@app.route("/api/v1/entries/<int:entryId>", methods=["GET"])
def get_single_entry(entryId):
    """ Retrieves specified entry from the list of entries"""
    if entries == []:
        return jsonify("There are no entries yet"),200
    else:
        for x in entries:
            if x["id"] == entryId:
                return jsonify({"You have retrieved":x}),200

@app.route('/api/v1/entries', methods=['POST'])
def add_entry():
    """ Adds an entry to to the list of entries"""
    entry = request.get_json()
    entry_keys = ["title","content","date","id"]
    for key in entry:
        # Checks whether the inputed data is valid
        if key not in entry_keys:
            return jsonify("Please enter valid data"),200
        # Checks whether the id inputed already exists
        elif entry in entries:
            if entry["id"] == entry[key]:
                return jsonify("That id is already taken"),200
        # Checks whether any field has no content
        elif entry[key] == "":
            return jsonify("One of the fields is empty"),200
    # Adds the inputed entry to the entries list
    entries.append(entry)
    return jsonify({'Entries': entries}),201

@app.route('/api/v1/entries/<int:entryId>', methods=["PUT"])
def edit_entry(entryId):
    """ Edits a specified entry"""
    if entries == []:
        return jsonify("There are no entries in your diary"),200
    else:
        for x in entries:
            if x["id"] == entryId:
                edited_entry = request.get_json()
                x["content"] = edited_entry["content"]
                x["title"] = edited_entry["title"]
        return jsonify ({"Your edited entry": x}),200

@app.route("/api/v1/entries/<int:entryId>", methods=["DELETE"])
def delete_entry(entryId):
    """ Deletes an entry from a list of entries"""
    if entries == []:
        return jsonify("There are no entries in your diary"),200
    else:
        for x in entries:
            if x["id"] == entryId:
                entries.remove(x)
        return jsonify ({"Your deleted entry": x}),200
