# clean.py

import sqlite3

connection = sqlite3.connect("Music.db")
cursor = connection.cursor()

# Drops all tables in Music.db

cursor.execute("""
DROP TABLE IF EXISTS Person
""")

cursor.execute("""
DROP TABLE IF EXISTS Platform
""")

cursor.execute("""
DROP TABLE IF EXISTS Song
""")

cursor.execute("""
DROP TABLE IF EXISTS Income
""")

connection.commit()
connection.close()