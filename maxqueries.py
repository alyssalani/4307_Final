# maxqueries.py

#!/usr/bin/env python3
import sqlite3
import sys

connection = sqlite3.connect("Music.db")
cursor = connection.cursor()

cursor.execute("""
SELECT first_name, age, weight, genre 
FROM PERSON
WHERE first_name == 'max'
AND genre == 'metal'
""")
userList = cursor.fetchall()

for x in userList:
    name = str(x[0])
    age = str(x[1])
    weight = str(x[2])
    print(name + " " + age + " " + weight)

connection.commit()
connection.close()
