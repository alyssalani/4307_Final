# 4307_Final
## Music Preferences
By: Alyssa Ponce, Max Stetter, Benjamin Jenks

## Description
Discover what kind of people like what kind of music!

#Tables
Person, Income, Event, Song, Platform

#Instructions

##### Quick Start
This quick start will get you going from scratch or if you simply want to have a clean slate.

1. Clean the DB
clean.py drops the following tables: Platform, Person, Income, Song.

```
python3 clean.py
```

2. Create the DB
createDatabase.py creates the Music.DB DataBase.

```
python3 createDatabase.py
```

3. Generate and Populate the Platform Table
gen_and_pop_platform.py will generate the platforms and insert them into the Platform table in Music.db

```
python3 gen_and_pop_platform.py
```

4. Everything!
Running this file will generate and populate for both people and income categories. 
(Make sure to enter the same number for people and incomes...)

```
python3 everything.py
```