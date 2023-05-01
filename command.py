#!/usr/bin/env python3

import sqlite3
import sys

command = sys.argv[1]
connection = sqlite3.connect("Music.db")
cursor = connection.cursor()
match command:
    case 'richest':
        rows = cursor.execute("""SELECT first_name, last_name, genre, state, income FROM Person, Income
        WHERE Person.personID = Income.personID
        ORDER BY income DESC""").fetchall()
        for i in rows:
            print(i)
        connection.commit()
        connection.close()
    case 'nearby':
        rows2 = cursor.execute("""SELECT first_name, last_name, state, genre
        FROM Person
        ORDER BY state, genre
        """).fetchall()
        for j in rows2:
            print(j)
    case 'recommended':
        id = sys.argv[1]
        cursor.execute("""
        SELECT song_name, artistName, Song.genre FROM Song, Person 
        WHERE Song.genre = Person.genre AND Person.personID = ?""", id)
        userList = cursor.fetchall()

        for x in userList:
            print(x)
        
    case 'platforms':
        cursor.execute("""
        SELECT platform_name Platform, cost Price, AVG(Income) Average_Income
        FROM Platform, Income, Person
        WHERE Income.personID=Person.personID AND Person.platform = platform_name
        GROUP BY platform_name
        ORDER BY Average_income""")
        userList = cursor.fetchall()
        for x in userList:
            print(x)
      
    case 'popularGenre':
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
