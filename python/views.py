from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app)

