from flask import Flask, render_template,jsonify,request
app = Flask(__name__)

entries = [
    {"entry1":"content1"},
    {"entry2":"content2"},
    {"entry3":"content3"}]

@app.route("/entries", methods=["GET"])
def entry():
    abc = [x for a in entries for x in a.keys()]
    return jsonify({"entries":abc})

@app.route("/entries/<string:entryId>")
def single(entryId):
    for x in entries:
        for a,b in x.iteritems():
            if a == entryId:
                return b
    return jsonify(b)
    




if __name__ == "__main__":
    app.run(debug=True)