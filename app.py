import os

from flask import Flask, request, abort, Response

from utils import build_query
from exceptions import QueryError, FilePathError

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST", "GET"])
def perform_query() -> Response:
    data_name = request.args.get('file_name')
    cmd1 = request.args.get('cmd1')
    value1 = request.args.get('value1')
    cmd2 = request.args.get('cmd2')
    value2 = request.args.get('value2')

    if not (cmd1 and value1 and data_name):
        abort(400, QueryError.message)

    file_path = os.path.join(DATA_DIR, data_name)
    if not os.path.exists(file_path):
        abort(400, FilePathError.message)

    with open(file_path) as file:
        result = build_query(cmd1, value1, file)
        if cmd2 and value2:
            result = build_query(cmd2, value2, result)

    return app.response_class("\n".join(result), content_type="text/plain")