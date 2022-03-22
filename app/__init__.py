from xml.etree.ElementInclude import include
from flask  import Flask, jsonify, request
from .services import read_json, write_json
from .exc import DontIncludedDataError
app = Flask(__name__)


@app.get("/user")
def get_users():
   return { "data": read_json()},200

@app.post("/user")
def post_user():
    data = request.get_json()
    read_json()
    try:
        if "nome" not in data or "email" not in data:
            raise DontIncludedDataError
        else:
            result = write_json(data)
            if 'error' in result:
                return jsonify(result), 409
            elif "wrong_fields" in result:
                return jsonify(result), 400
            else:
                return jsonify(result), 201

    except DontIncludedDataError as err:
        return err.message, 400
     
