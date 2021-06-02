from pyaadhaar import deocde
from flask import Flask, jsonify, request

app = Flask(__name__)


def decodeaadhaar(qrdata):
    obj = deocde.AadhaarSecureQr(qrdata)
    return obj.decodeddata()


@app.route("/", methods=['GET'])
def dummy_api():
    name = request.args.get("name")
    return jsonify(data=decodeaadhaar(int(name))), 200


@app.route('/post/', methods=['POST', 'PUT', 'DELETE'])
def post_something():
    return "This service works only for GET With attached aadhaar qr data"


if __name__ == "__main__":
    app.run()






