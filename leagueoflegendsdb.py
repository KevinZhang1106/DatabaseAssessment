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
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, winrate FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY winrate DESC"
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

def insert_data(new_champion_name, new_role, new_strongest_lane, new_winrate, new_base_hp, new_base_ad, new_base_armor, new_base_magicresist, new_base_attackspeed, new_attackrange, new_movespeed):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    
    cursor.execute("SELECT role_id FROM Role WHERE role_name = ?", (new_role,))
    role_id = cursor.fetchone()
    if role_id is None:
        print(f"{new_role} is not a valid input")
        db.close()
        return
    role_id = role_id[0]
    
    cursor.execute("SELECT lane_id FROM Lanes WHERE lane_name = ?", (new_strongest_lane,))
    lane_id = cursor.fetchone()
    if lane_id is None:
        print(f"{new_strongest_lane} is not a valid input")
        db.close()
        return
    lane_id = lane_id[0]
    
    sql = "INSERT INTO Champions (champion_name, role, strongest_lane, winrate, base_hp, base_ad, base_armor, base_magicresist, base_attackspeed, attackrange, movespeed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (new_champion_name, role_id, lane_id, new_winrate, new_base_hp, new_base_ad, new_base_armor, new_base_magicresist, new_base_attackspeed, new_attackrange, new_movespeed)
    cursor.execute(sql, values)
    print("New champion data inserted successfully.")
    
    db.commit()
    db.close()

def delete_data(delete_champion_name):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (delete_champion_name,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{delete_champion_name} is not a champion in the database")
        db.close()
        return
    
    sql = "DELETE FROM Champions WHERE champion_name=?"
    cursor.execute(sql, (delete_champion_name,))
    print("Champion data deleted successfully.")

    db.commit()
    db.close()

def update_data_name(which_update_champion, update_champion_name):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET champion_name= ? WHERE champion_name=?"
    values = (update_champion_name, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_role(which_update_champion, update_role):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    cursor.execute("SELECT role_id FROM Role WHERE role_name = ?", (update_role))
    role_id = cursor.fetchone()
    if role_id is None:
        print(f"{update_role} is not a valid input")
        db.close()
        return
    role_id = role_id[0]

    sql = "UPDATE Champions SET role= ? WHERE champion_name=?"
    values = (role_id, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_lane(which_update_champion, update_lane):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    cursor.execute("SELECT lane_id FROM Lanes WHERE lane_name = ?", (update_lane))
    lane_id = cursor.fetchone()
    if lane_id is None:
        print(f"{update_lane} is not a valid input")
        db.close()
        return
    lane_id = lane_id[0]

    sql = "UPDATE Champions SET strongest_lane = ? WHERE champion_name = ?"
    values = (lane_id, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_winrate(which_update_champion, update_winrate):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET winrate = ? WHERE champion_name = ?"
    values = (update_winrate, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_hp(which_update_champion, update_hp):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET base_hp = ? WHERE champion_name = ?"
    values = (update_hp, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_ad(which_update_champion, update_ad):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET base_ad = ? WHERE champion_name = ?"
    values = (update_ad, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_armor(which_update_champion, update_armor):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET base_armor = ? WHERE champion_name = ?"
    values = (update_armor, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_magicresist(which_update_champion, update_magicresist):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET base_magicresist = ? WHERE champion_name = ?"
    values = (update_magicresist, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_attackspeed(which_update_champion, update_attackspeed):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET base_attackspeed = ? WHERE champion_name = ?"
    values = (update_attackspeed, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_attackrange(which_update_champion, update_attackrange):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET attackrange = ? WHERE champion_name = ?"
    values = (update_attackrange, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_data_movespeed(which_update_champion, update_movespeed):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (which_update_champion,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        print(f"{which_update_champion} is not a champion in the database\n Update failed.")
        db.close()
        return

    sql = "UPDATE Champions SET movespeed = ? WHERE champion_name = ?"
    values = (update_movespeed, which_update_champion)
    cursor.execute(sql, values)
    db.commit()
    db.close()

def champions_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_name FROM Champions"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Champion names\n")
    for champion in results:
        print(champion[0])
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
                       "Type 0 to insert a new row to the database\n"
                       "Type 11 to delete a row in the database\n"
                       "Type 12 to update data in the database\n"
                       "Type nothing to exit\n"
                       "You: ")
    
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
    elif user_input == "0":
        new_champion_name = input("Enter champion name: ")
        new_role = input("role? (capitalisation is important)\n"
                         "assassin, mage, tank, marksmen, support, fighter\n"
                         "You: "
                         )
        new_lane = input("strongest lane? (capitalisation is important)\n"
                         "mid, bottom, top, jungle\n"
                         "You: "
                         )
        new_winrate = input("Enter winrate: ")
        new_hp = input("Enter base hp: ")
        new_ad = input("Enter base ad: ")
        new_armor = input("Enter base armor: ")
        new_magicresist = input("Enter base magicresist: ")
        new_attackspeed = input("Enter base attackspeed: ")
        new_attackrange = input("Enter base attackrange: ")
        new_movespeed = input("Enter base movespeed: ")
        
        insert_data(new_champion_name, new_role, new_lane, new_winrate, new_hp, new_ad, new_armor, new_magicresist, new_attackspeed, new_attackrange, new_movespeed)
    elif user_input == "11":
        champions_name()
        delete_champion_name = input("Enter champion you would like to delete: ")
        delete_data(delete_champion_name)
    elif user_input == "12":
        champions_name()
        which_update_champion = input("Enter the champion you would like to update: ")
        column_name = input("Which column would you like to update\n"
                            "name, role, lane, winrate, hp, ad, armor, magicresist, attackspeed, attackrange, movespeed\n"
                            "You: "
                            )
        if column_name == "name":
            update_champion_name = input("Enter new champion name: ")
            update_data_name(which_update_champion, update_champion_name)
        elif column_name == "role":
            update_role = input("Enter new role: ")
            update_data_role(which_update_champion, update_role)
        elif column_name == "lane":
            update_lane = input("Enter new lane: ")
            update_data_lane(which_update_champion, update_lane)
        elif column_name == "winrate":
                update_winrate = input("Enter new winrate: ")
                update_data_winrate(which_update_champion, update_winrate)
        elif column_name == "hp":
            update_hp = input("Enter new base hp: ")
            update_data_hp(which_update_champion, update_hp)
        elif column_name == "ad":
            update_ad = input("Enter new base ad: ")
            update_data_ad(which_update_champion, update_ad)
        elif column_name == "armor":
            update_armor = input("Enter new base armor: ")
            update_data_armor(which_update_champion, update_armor)
        elif column_name == "magicresist":
            update_magicresist = input("Enter new base magic resist: ")
            update_data_magicresist(which_update_champion, update_magicresist)
        elif column_name == "attackspeed":
            update_attackspeed = input("Enter new base attack speed: ")
            update_data_attackspeed(which_update_champion, update_attackspeed)
        elif column_name == "attackrange":
            update_attackrange = input("Enter new base attack range: ")
            
    elif user_input == "":
        break
    else:
        print("\nThat was not a valid input, Try again\n")