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
        song = x[0]
        artist = x[1]
        genre = x[2]
        cursor.execute("INSERT INTO " + table_name + " (song_name,artistName,genre) VALUES('{}', '{}', '{}')".format(song, artist, genre))
        connection.commit()
        
    
populate_table("songs.csv", "Song")
