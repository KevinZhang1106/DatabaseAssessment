# docstring - Kevin Zhang league of legends database application
import sqlite3

# variables
DATABASE = "champions.db"

# functions


def champions_info():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        Winrate         hp            ad           armor        magicresist  attackspeed     range         movespeed")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<16}{champion[5]:<14}{champion[6]:<13}{champion[7]:<13}{champion[8]:<13}{champion[9]:<16}{champion[10]:<14}{champion[11]}")
    db.close()


def champions_winrate():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY winrate DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        Winrate         ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<16}")
    db.close()


def champions_hp():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY base_hp DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        hp            ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[5]:<14}")
    db.close()


def champions_ad():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY base_ad DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        ad           ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[6]:<13}")
    db.close()    


def champions_armor():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY base_armor DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        armor        ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[7]:<13}")
    db.close()


def champions_magicresist():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY base_magicresist DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        magicresist  ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[8]:<13}")
    db.close()


def champions_attackspeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY base_attackspeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        attackspeed     ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[9]:<16}")
    db.close()


def champions_range():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY attackrange"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        range         ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[10]:<14}")
    db.close()


def champions_movespeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM champions ORDER BY movespeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name           Class       Lane        movespeed")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[11]}")
    db.close()



