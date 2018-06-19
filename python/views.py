from models import Article

def articles():
    return Article.query.all()
