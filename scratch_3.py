from flask import Flask, jsonify
# from flask_restful import Api, Resource, reqparse
# import pandas as pd

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello world"
country_code = {'India': '0091',
                'Australia': '0025',
                    'Nepal': '00977'}
@app.route("/codes/<string:country>", methods = ["GET"])
def get(country):
    return jsonify({'Codes111111111': country_code[country]})

if __name__ == "__main__":
    app.run(debug= True)
