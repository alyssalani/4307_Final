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
    #print(rows)
    for x in rows:
        platform = x[0]
        first_name = x[1]
        last_name = x[2]
        genre = x[3]
        age = x[4]
        state = x[5]
        weight = x[6]
        height = x[7]
        cursor.execute("INSERT INTO " + table_name + " (platform,first_name,last_name,genre,age,state,weight,height) VALUES(?, ?, ?, ?, ? ,?, ?, ?)", (platform, first_name, last_name, genre, age, state, weight, height))
        connection.commit()
        
    
populate_table("people.csv", "Person")
