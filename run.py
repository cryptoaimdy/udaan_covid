
import flask
from flask import Flask, request, jsonify
from flask_restplus import Api
import requests
from werkzeug import datastructures
from db_model import Database






app = Flask(__name__)

@app.route("/registerUser", methods = ["POST"])
def post():
    print("hello")
        # if request.args:
        #     print("yes")
    data = request.json

    if data.get("name") in ["", None]:
        return {
            "code": 400,
            "message": "name cannot be null"
        }

    elif data.get("phoneNumber") in ["", None]:
        return {
            "code": 400,
            "message": "PH cannot be null"
        }

    elif data.get("pinCode") in ["", None]:
        return {
            "code": 400,
            "message": "PIN cannot be null"
        }



    result = Database().store(data)

    return result


@app.route("/selfassessment", methods = ["POST"])
def asses():
    print("hello")
        # if request.args:
        #     print("yes")
    data = request.json
    result = Database().assessment_data(data)

    return result






if __name__ == "__main__":
    app.run()
