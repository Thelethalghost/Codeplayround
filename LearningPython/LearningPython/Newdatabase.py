import mysql.connector as cntr

db = cntr.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "test"
)

cur = db.cursor()

# cur.execute("CREATE DATABASE test")
# cur.execute("CREATE TABLE Books(Name VARCHAR(50), Author VARCHAR(50) , Price int UNSIGNED, id int PRIMARY KEY  AUTO_INCREMENT)")
# cur.execute("INSERT INTO Books(Name,Author,Price) VALUES (%s,%s,%s)",("Trials of Apollo: The Dark Prphecy","Rick Riordan",300))
# db.commit()
# cur.execute("SELECT * FROM Books WHERE Author = 'Rick Riordan' ORDER BY id DESC ")
cur.execute("ALTER TABLE Books ADD COLUMN ")

for i in cur:
    print(i)