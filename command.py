#!/usr/bin/env python3

import sqlite3
import sys

command = sys.argv[1]
connection = sqlite3.connect("Music.db")
cursor = connection.cursor()
match command: 
  
  case 'richest':
    
  case 'nearby':
    
  case 'recommended':
    
  case 'platforms':
    
  case 'popularGenre':
