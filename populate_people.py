#!/usr/bin/python3
import sqlite3
import csv
connection = sqlite3.connect("Music.db")
cursor = connection.cursor()

def populate_table(csv_file, table_name):
    rows = []
    with open(csv_file, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for i in csvreader:
            rows.append(i)
    print(rows)
    for x in rows:
        platform = x[0]
        name = x[1]
        genre = x[2]
        age = x[3]
        state = x[4]
        weight = x[5]
        height = x[6]
        cursor.execute("INSERT INTO " + table_name + " (platform,name,genre,age,state,weight,height) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(platform, name, genre, age, state, weight, height))
        connection.commit()
        
    
populate_table("people.csv", "Person")
