from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artist (name)"