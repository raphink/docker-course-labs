from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

################
#### config ####
################

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
      return {
          'products': ['geomapfish', 'georchestra', 'geonetwork' ]
      }

# routes
api.add_resource(Product, '/')


app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
