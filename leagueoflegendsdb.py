import sqlite3


DATABASE = "champions.db"

db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM champions"
cursor.execute(sql)
results = cursor.fetchall()
for champion in results:
    print(champion)
db.close()
