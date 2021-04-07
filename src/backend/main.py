import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from PathFinder import aStarPath

app = Flask(__name__)
CORS(app)

# Routes
@app.route("/path-a-star", methods=["POST"])
def getPathAStar():
    res = {}

    try:

        body = request.get_json()

        nodeStart = body["nodeStart"]
        nodeDestination = body["nodeDestination"]
        nodes = body["nodes"]
        adj = body["adj"]

        res = aStarPath(nodeStart, nodeDestination, nodes, adj)

    except:

        res = {"error": True}

    finally:
        
        return jsonify(res)

PORT = 5000
if __name__ == "__main__":
    app.run(host = "localhost", port = PORT, debug = True)