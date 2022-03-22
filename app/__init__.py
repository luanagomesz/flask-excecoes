from flask  import Flask, jsonify, request
from .services import read_json, write_json

app = Flask(__name__)


@app.get("/user")
def get_users():
   return { "data": read_json()},200

@app.post("/user")
def post_user():
    data = request.get_json()
    read_json()
    result = write_json(data)
    if 'error' in result:
        return jsonify(result), 409
    elif "wrong_fields" in result:
        return jsonify(result), 400
    else:
        return jsonify(result), 201
