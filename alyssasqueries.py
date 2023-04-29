#!/usr/bin/env python3
import sqlite3
import sys

connection = sqlite3.connect("Social_Network.db")
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM Person""")
userList = cursor.fetchall()

for x in userList:
	print(x[0])

connection.commit()
connection.close()
