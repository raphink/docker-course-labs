from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json

################
#### config ####
################
app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app)

import views



class Product(Resource):
    def get(self):
      return {
          'products': ['geomapfish', 'georchestra', 'geonetwork' ]
      }

# routes
api.add_resource(Product, '/')

@app.route('/db')
def index():
    names = []
    for result in views.articles():
        names.append(result.article_name)
    return json.dumps(names) # '[



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
