#!/usr/bin/env python3

import sqlite3
import sys

connection = sqlite3.connect("Music.db")
cursor = connection.cursor()
command = sys.argv[1]
if (command== 'richest'):
    rows = cursor.execute("""SELECT first_name, last_name, genre, state, income FROM Person, Income
        WHERE Person.personID = Income.personID
        ORDER BY income DESC""").fetchall()
    for i in rows:
        print(i)
    connection.commit()
    connection.close()
elif(command== 'nearby'):
    id = sys.argv[2]
    rows2 = cursor.execute("""SELECT Person.first_name, Person.last_name, Person.state, Person.genre
    FROM Person Join Person p ON p.state = Person.state
    WHERE p.personID =?
    ORDER BY Person.state, Person.genre
        """, id).fetchall()
    for j in rows2:
        print(j)
    connection.commit()
    connection.close()

elif(command=='recommended'):
    id = sys.argv[2]
    cursor.execute("""
        SELECT song_name, artistName, Song.genre FROM Song, Person
        WHERE Song.genre = Person.genre AND Person.personID = ?""", id)
    userList = cursor.fetchall()

    for x in userList:
        print(x)
    connection.commit()
    connection.close()

elif(command== 'platforms'):
    cursor.execute("""
        SELECT platform_name Platform, cost Price, AVG(Income) Average_Income
        FROM Platform, Income, Person
        WHERE Income.personID=Person.personID AND Person.platform = platform_name
        GROUP BY platform_name
        ORDER BY Average_income DESC""")
    userList = cursor.fetchall()
    for x in userList:
        print(x)

elif(command== 'popularGenre'):
    cursor.execute("""
        SELECT genre, COUNT(genre) AS count
        FROM PERSON
        GROUP BY genre
        ORDER BY count DESC
        """)
    userList = cursor.fetchall()
    for x in userList:
        name = str(x[0])
        genre = str(x[1])
        print(name + ": " + genre)
else:
    print("Not a valid command")
