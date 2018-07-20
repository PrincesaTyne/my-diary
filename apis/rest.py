from flask import Flask, jsonify, request

app = Flask(__name__)

entries = [
    {'entryId1':'content1'},
    {'entryId2':'content2'},
    {'entryId3':'content3'}]

@app.route("/api/v1/entries", methods=["GET"])
def ids():
    abc = [x for a in entries for x in a.keys()]
    return jsonify({"Entries":abc})

@app.route("/api/v1/entries/<string:entryId>", methods=["GET"])
def single_entry(entryId):
    for x in entries:
        for a,b in x.iteritems():
            if a == entryId:
                return b
    return jsonify(b)

@app.route('/api/v1/entries', methods=['POST'])
def add_entry():
    entry = request.get_json("ent")
    entries.append(entry)
    return jsonify({'Entries': entries})

@app.route('/api/v1/entries/<string:entryId>', methods=["PUT"])
def edit_entry(entryId):
    for x in entries:
        for a in x.keys():
            if a == entryId:
                x[entryId] = request.get_json(entryId)
    return jsonify ({"your entries": entries})

@app.route('/api/v1/entries/<string:entryId>', methods=["DELETE"])
def remove_entry(entryId):
    for x in entries:
        for a in x.keys():
            if a == entryId:
                entries.remove(x)
    return jsonify({"Your entries": entries})

if __name__ == "__main__":
    app.run(debug= True, port=3000)