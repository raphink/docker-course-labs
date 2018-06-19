from api import db
from models import Article


# create the database and the database table
db.create_all()

# insert recipe data
ar1 = Article('Geomapfish', 'magnifique')
ar2 = Article('OpenLayers', 'aussi')
db.session.add(ar1)
db.session.add(ar2)


# commit the changes
db.session.commit()