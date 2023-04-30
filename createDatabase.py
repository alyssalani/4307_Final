#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect("Music.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Person (
    personID        INTEGER PRIMARY KEY,
    platform     TEXT NOT NULL,
    first_name            TEXT NOT NULL,
    last_name            TEXT NOT NULL,
    genre           TEXT NOT NULL,
    age             INTEGER NOT NULL,
    state           TEXT NOT NULL,
    weight          INTEGER NOT NULL,
    height          INTEGER NOT NULL
)
""")
               
cursor.execute("""
CREATE TABLE IF NOT EXISTS Income (
    personID        INTEGER PRIMARY KEY,
    income          INTEGER NOT NULL,
    status          TEXT NOT NULL,
    FOREIGN KEY(personID) REFERENCES Person(personID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Song(
    songID       INTEGER PRIMARY KEY,
    song_name     TEXT NOT NULL,
    artistName    INTEGER NOT NULL,
    genre         TEXT NOT NULL,
    FOREIGN KEY(genre) REFERENCES Person(genre)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Platform(
    platformID  INTEGER NOT NULL,
    platform_name  TEXT NOT NULL,
    cost INTEGER NOT NULL,
    PRIMARY KEY(platformID)
    FOREIGN KEY(platformID) REFERENCES Person(platformID)
)
""")


connection.commit()
connection.close()


### OLD ###
'''

cursor.execute("""
CREATE TABLE IF NOT EXISTS Person (
    personID        INTEGER PRIMARY KEY,
    platformID     INTEGER NOT NULL,
    name            TEXT NOT NULL,
    genre           TEXT NOT NULL,
    age             INTEGER NOT NULL,
    state           TEXT NOT NULL,
    weight          INTEGER NOT NULL,
    height          INTEGER NOT NULL,
    PRIMARY KEY(personID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Income (
    personID        INTEGER PRIMARY KEY,
    income          INTEGER NOT NULL,
    status          TEXT NOT NULL,
    FOREIGN KEY(personID) REFERENCES Person(personID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Song(
    songID       INTEGER PRIMARY KEY,
    song_name     TEXT NOT NULL,
    artistName    INTEGER NOT NULL,
    genre         TEXT NOT NULL,
    PRIMARY KEY(songID),
    FOREIGN KEY(genre) REFERENCES Person(genre)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Platform(
    platformID  INTEGER NOT NULL,
    platform_name  TEXT NOT NULL,
    cost INTEGER NOT NULL,
    PRIMARY KEY(platformID)
    FOREIGN KEY(platformID) REFERENCES Person(platformID)
)
""")


'''
