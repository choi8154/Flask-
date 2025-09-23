from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from resources.api import Item, items


app = Flask(__name__)

api = Api(app)

@app.route("/item/")
def get():
    return items


api.add_resource(Item, "/item/<string:name>")

if __name__=="__main__":
    app.run(debug=True)