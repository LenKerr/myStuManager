import sqlite3
import os

if os.path.exists('stu.db'):
	print('database file is already exist')
	exit(0)

conn = sqlite3.connect('stu.db')
print ("Opened database successfully");
c = conn.cursor()
c.execute('''create table STU
       (id text primary key,
       name text,
       gender text,
       grade text,
       major text,
       score text);''')
print ("Table created successfully");
conn.commit()
conn.close()