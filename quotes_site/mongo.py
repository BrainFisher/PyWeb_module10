from quotes_app.models import Quote
import os
import django
from django.conf import settings
import psycopg2
from pymongo import MongoClient

# Налаштуйте Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_site.settings')
django.setup()

# Підключення до бази даних MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
mongo_db = mongo_client['database_name']
mongo_collection = mongo_db['collection_name']

# Підключення до бази даних Postgres
postgres_conn = psycopg2.connect(
    dbname='my_postgres_db',
    user='postgres',
    password='pass',
    host='localhost'
)
postgres_cursor = postgres_conn.cursor()

# Отримання даних з MongoDB та вставка їх у базу даних Postgres
for mongo_quote in mongo_collection.find():
    # Створення екземпляру моделі Django з отриманих даних
    quote = Quote(
        text=mongo_quote['text'],
        author=mongo_quote['author']
    )
    # Збереження об'єкта у базі даних Postgres
    quote.save()

# Закриття з'єднань
mongo_client.close()
postgres_cursor.close()
postgres_conn.close()
