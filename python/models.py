from api import db

class Article(db.Model):

    __tablename__ = "articles"

    article_id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(200), unique=False, nullable=True)
    article_desc = db.Column(db.String(200), unique=False, nullable=True)

    def __init__(self, title, description):
        self.article_name = title
        self.article_desc = description

    def __repr__(self):
        return '<title {}'.format(self.article_name)