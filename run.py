from flask import Flask
from flask_restplus import Api
from db_model import Database






app = Flask(__name__)

@app.route("/registerUser", methods = ["POST", "GET"])
def post():
    print("hello")
    result = Database().model_return()
    return result




if __name__ == "__main__":
    app.run()
