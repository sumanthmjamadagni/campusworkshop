"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13asrh4hstbhh8q7fg-a.oregon-postgres.render.com",
        database="todo_688k",
        user="root",
        password="23riGqtC8Y00PgMqBzqcI87NLqnDrO5A")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
