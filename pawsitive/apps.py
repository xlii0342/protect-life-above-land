from django.apps import AppConfig

from flask import Flask, jsonify 
import psycopg2
import os

app = Flask(__name__)

# Heroku PostgreSQL connection string from env variable
DATABASE_URL = os.environ.get("DATABASE_URL")

class PawsitiveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pawsitive"

