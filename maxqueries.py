# maxqueries.py

#!/usr/bin/env python3
import sqlite3
import sys


list_of_commands = ["popular_genre", "poop"]

command = ""
if len(sys.argv) > 1:
    command = sys.argv[1]

def query(command):
    connection = sqlite3.connect("Music.db")
    cursor = connection.cursor()

    if command == list_of_commands[0]:
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
    elif command == list_of_commands[1]:
        print('I pooped.')
    else:
        print('NOT a valid command! \n \nValid commands are:')
        for valid_command in list_of_commands:
            print(valid_command)
    connection.commit()
    connection.close()


query(command)