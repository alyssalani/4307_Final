#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("Music.db")
cursor = connection.cursor()


# first query, richest people and what genre of music is their favorite
rows = cursor.execute("""SELECT first_name, last_name, genre, state, income FROM Person, Income
WHERE Person.personID = Income.personID
ORDER BY income DESC""").fetchall()
for i in rows:
    print(i)

#second query, people in the same state with  similar taste in music
rows2 = cursor.execute("""SELECT first_name, last_name, state, genre
        FROM Person
        GROUP BY state
        ORDER BY genre""").fetchall()
for j in rows2:
    print(j)

