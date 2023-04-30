#!/usr/bin/env python3
import sqlite3
import sys

connection = sqlite3.connect("Music.db")
cursor = connection.cursor()
id = sys.argv[1]
cursor.execute("""
SELECT song_name, artistName, Song.genre FROM Song, Person 
WHERE Song.genre = Person.genre AND Person.personID = 2""", id)

userList = cursor.fetchall()

for x in userList:
        print(x)

connection.commit()
connection.close()
