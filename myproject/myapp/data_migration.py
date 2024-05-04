# myapp/data_migration.py

from myapp.models import Author, Quote
from pymongo import MongoClient


def migrate_data_from_mongodb_to_postgres():
    
    client = MongoClient('mongodb://localhost:27017/')
    db = client['database_name']

    
    for author_data in db['authors'].find():
        author = Author.objects.create(name=author_data['name'])
        for quote_data in db['quotes'].find({'author_id': author_data['_id']}):
            Quote.objects.create(author=author, text=quote_data['text'])



migrate_data_from_mongodb_to_postgres()
