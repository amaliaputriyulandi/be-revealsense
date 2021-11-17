from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
#melakukan perubahan

app = Flask(__name__)
CORS(app)
#app.config["SQLALCHEMY_DATABASE_URI"]='postgres'

#db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello WorlD"

if __name__ == '__main__':
    app.run(debug=True)