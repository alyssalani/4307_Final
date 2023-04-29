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
        print('x: ', x)
        yearly_income = x[0]
        status = x[1]
        cursor.execute("INSERT INTO " + table_name + " (income,status) VALUES('{}', '{}')".format(yearly_income, status))
        connection.commit()
        
    
populate_table("incomes.csv", "Income")
