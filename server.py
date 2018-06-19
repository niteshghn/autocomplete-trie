from flask import Flask, jsonify, request

from connector import Connector
from operator import itemgetter
app = Flask(__name__)


@app.route('/auto')
def hello_world():
    query = request.args.get("q", '')
    results = []  # must be list of dicts: [{"name": "foo"}, {"name": "bar"}]
    matches = Connector.search(query.lower())
    results = sorted([{'name': match, 'score': (len(query)/len(match))*10} for match in matches], key=itemgetter('score'), reverse=True)
    resp = jsonify(results=results[:10])  # top 10 results
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp