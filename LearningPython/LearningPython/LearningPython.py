import mysql.connector as sql

db = sql.connect(host = "localhost",
                 user = "root",
                 passwd = "root",
                 database = "testdatabase")

cur = db.cursor()
#cur.execute("CREATE DATABASE testdatabase")
cur.execute("CREATE TABLE book(Name of the book VARCHAR(50),Author VARCHAR(50),Price int,id var PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#cur.execute("INSERT INTO book  VALUES (%s,%s,%s)",("Wolf Brother","Michelle Paver",300))
db.commit()