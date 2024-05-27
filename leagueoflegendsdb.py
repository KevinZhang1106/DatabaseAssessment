# docstring - Kevin Zhang league of legends database application
import sqlite3

# variables
DATABASE = "champions.db"

# functions

# displays all champions information
def champions_info():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        Winrate         hp            ad           armor        magicresist  attackspeed     range         movespeed")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<16}{champion[5]:<14}{champion[6]:<13}{champion[7]:<13}{champion[8]:<13}{champion[9]:<16}{champion[10]:<14}{champion[11]}")
    print("\n")
    db.close()

# sorts champion in order of winrate highest to lowest
def champions_winrate():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY winrate DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        Winrate         ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<16}")
    print("\n")
    db.close()

# sorts champion in order of hp highest to lowest
def champions_hp():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_hp DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        hp            ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[5]:<14}")
    print("\n")
    db.close()

# sorts champion in order of ad highest to lowest
def champions_ad():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_ad DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        ad           ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[6]:<13}")
    print("\n")
    db.close()    

# sorts champion in order of armor highest to lowest
def champions_armor():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_armor DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        armor        ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[7]:<13}")
    print("\n")
    db.close()

# sorts champion in order of magicresist highest to lowest
def champions_magicresist():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_magicresist DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        magicresist  ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[8]:<13}")
    print("\n")
    db.close()

# sorts champion in order of attackspeed highest to lowest
def champions_attackspeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_attackspeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        attackspeed     ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[9]:<16}")
    print("\n")
    db.close()

# sorts champion in order of range highest to lowest
def champions_range():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY attackrange DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        range         ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[10]:<14}")
    print("\n")
    db.close()

# sorts champion in order of movespeed highest to lowest
def champions_movespeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY movespeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        movespeed")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[11]}")
    print("\n")
    db.close()


while True:
    user_input = input("Type 1 to display all the champions information\n"
                    "Type 2 to display champion winrate highest to lowest\n"
                    "Type 3 to display champion hp highest to lowest\n"
                    "Type 4 to display champion ad highest to lowest\n"
                    "Type 5 to display champion armor highest to lowest\n"
                    "Type 6 to display champion magic resist highest to lowest\n"
                    "Type 7 to display champion attack speed highest to lowest\n"
                    "Type 8 to display champion range highest to lowest\n"
                    "Type 9 to display champion movespeed highest to lowest\n"
                    "Type nothing to exit\n"
                    "\n")
                    
    if user_input == "1":
        champions_info()
    elif user_input == "2":
        champions_winrate()
    elif user_input == "3":
        champions_hp()
    elif user_input == "4":
        champions_ad()
    elif user_input == "5":
        champions_armor()
    elif user_input == "6":
        champions_magicresist()
    elif user_input == "7":
        champions_attackspeed()
    elif user_input == "8":
        champions_range()
    elif user_input == "9":
        champions_movespeed()
    elif user_input == "":
        break
    else:
        print("\n")
        print("That was not a valid input, Try again")
        print("\n")

