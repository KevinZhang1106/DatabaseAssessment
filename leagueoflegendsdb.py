# docstring - Kevin Zhang league of legends database application
import sqlite3

DATABASE = "champions.db"

# functions

# prints all champions information
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

# prints champions name, role, lane and winrate in order of winrate highest to lowest
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

# prints champions name, role, lane and hp in order of hp highest to lowest
def champions_hp():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, base_hp FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_hp DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        hp            ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<14}")
    print("\n")
    db.close()

# prints champions name, role, lane and ad in order of ad highest to lowest
def champions_ad():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, base_ad FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_ad DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        ad           ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<13}")
    print("\n")
    db.close()    

# prints champions name, role, lane and armor in order of armor highest to lowest
def champions_armor():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, base_armor FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_armor DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        armor        ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<13}")
    print("\n")
    db.close()

# prints champions name, role, lane and magicresist in order of magicresist highest to lowest
def champions_magicresist():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, base_magicresist FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_magicresist DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        magicresist  ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<13}")
    print("\n")
    db.close()

# prints champions name, role, lane and attackspeed in order of attackspeed highest to lowest
def champions_attackspeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, base_attackspeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY base_attackspeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        attackspeed     ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]:<16}")
    print("\n")
    db.close()

# prints champions name, role, lane and range in order of range highest to lowest
def champions_range():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, attackrange FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY attackrange DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        range         ")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[10]:<14}")
    print("\n")
    db.close()

# prints champions name, role, lane and movespeed in order of movespeed highest to lowest
def champions_movespeed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT champion_id, champion_name, Role.role_name, Lanes.lane_name, movespeed FROM Champions JOIN Role ON Champions.role = Role.role_id JOIN Lanes ON Champions.strongest_lane = Lanes.lane_id ORDER BY movespeed DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\n")
    print("Name           Role        Lane        movespeed")
    for champion in results:
        print(f"{champion[1]:<15}{champion[2]:<12}{champion[3]:<12}{champion[4]}")
    print("\n")
    db.close()

# inserts data to the database based on users input and checks whether users input is valid
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
    print("\n")
    print("New champion data inserted successfully.")
    print("\n")
    
    db.commit()
    db.close()

# deletes a specific row of data from the database based on users input and checks whether users input is valid
def delete_data(delete_champion_name):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()    
    sql = "DELETE FROM Champions WHERE champion_name=?"
    cursor.execute(sql, (delete_champion_name,))
    print("\n")
    print("Champion data deleted successfully.")
    print("\n")

    db.commit()
    db.close()

# updates a champions name based on users input
def update_data_name(which_update_champion, update_champion_name):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET champion_name= ? WHERE champion_name=?"
    values = (update_champion_name, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions role based on users input
def update_data_role(which_update_champion, update_role):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT role_id FROM Role WHERE role_name = ?", (update_role,))
    role_id = cursor.fetchone()
    if role_id is None:
        print(f"{update_role} is not a valid input")
        db.close()
        return
    role_id = role_id[0]

    sql = "UPDATE Champions SET role= ? WHERE champion_name=?"
    values = (role_id, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions lane based on uers input
def update_data_lane(which_update_champion, update_lane):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT lane_id FROM Lanes WHERE lane_name = ?", (update_lane,))
    lane_id = cursor.fetchone()
    if lane_id is None:
        print(f"{update_lane} is not a valid input")
        db.close()
        return
    lane_id = lane_id[0]

    sql = "UPDATE Champions SET strongest_lane = ? WHERE champion_name = ?"
    values = (lane_id, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# uppdates a champions wineate based on users input
def update_data_winrate(which_update_champion, update_winrate):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET winrate = ? WHERE champion_name = ?"
    values = (update_winrate, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base hp based on users input
def update_data_hp(which_update_champion, update_hp):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET base_hp = ? WHERE champion_name = ?"
    values = (update_hp, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base ad based on users input
def update_data_ad(which_update_champion, update_ad):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET base_ad = ? WHERE champion_name = ?"
    values = (update_ad, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base armor based on users input
def update_data_armor(which_update_champion, update_armor):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET base_armor = ? WHERE champion_name = ?"
    values = (update_armor, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base magicresist based on users input
def update_data_magicresist(which_update_champion, update_magicresist):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET base_magicresist = ? WHERE champion_name = ?"
    values = (update_magicresist, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a chhampions base attack speed based on users input
def update_data_attackspeed(which_update_champion, update_attackspeed):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET base_attackspeed = ? WHERE champion_name = ?"
    values = (update_attackspeed, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base attack range based on uers input
def update_data_attackrange(which_update_champion, update_attackrange):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET attackrange = ? WHERE champion_name = ?"
    values = (update_attackrange, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# updates a champions base move speed based on users input
def update_data_movespeed(which_update_champion, update_movespeed):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "UPDATE Champions SET movespeed = ? WHERE champion_name = ?"
    values = (update_movespeed, which_update_champion)
    cursor.execute(sql, values)
    print("\n")
    print("Champion data updated successfully.")
    print("\n")
    db.commit()
    db.close()

# prints only the champion name
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

# checks whether champion name is already in the database and returns true or false based on result
def is_champion_real(placeholder,):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute("SELECT champion_name FROM Champions WHERE champion_name =?", (placeholder,))
    is_champion = cursor.fetchone()
    if is_champion is None:
        db.close()
        return False
    else:
        db.close()
        return True

# checks whether number can be turned into a float and returns true or false based on result
def is_decimal_number(placeholder):
    try:
        float(placeholder)
        return True
    except ValueError:
        return False

# MENU

# while loop that will keep running until user enters nothing
while True:
    # gives user list of all the things they can do
    user_input = input("1 = print all the champions information\n"
                       "2 = print champion winrate highest to lowest\n"
                       "3 = print champion hp highest to lowest\n"
                       "4 = print champion ad highest to lowest\n"
                       "5 = print champion armor highest to lowest\n"
                       "6 = print champion magic resist highest to lowest\n"            
                       "7 = print champion attack speed highest to lowest\n"
                       "8 = print champion range highest to lowest\n"
                       "9 = print champion movespeed highest to lowest\n"
                       "i = insert a new row to the database\n"
                       "d = delete a row in the database\n"
                       "u = update data in the database\n"
                       "enter nothing = exit\n"
                       "You: ")
    
    # checks if user input is valid and will run a function based on the user input, if not valid then will ask user to try again
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
    elif user_input == "i":
        # while loop that will keep running until user enters a unique champion name
        while True:
            new_champion_name = input("Enter champion name: ")
            if is_champion_real(new_champion_name):
                print("This champion already exists please enter a champion that is not already in the database")
            else:
                break
        # assigns variables to the users input used in functions above to user input
        new_role = input("role? (capitalisation is important)\n"
                         "assassin, mage, tank, marksmen, support, fighter\n"
                         "You: "
                         )
        new_lane = input("strongest lane? (capitalisation is important)\n"
                         "mid, bottom, top, jungle\n"
                         "You: "
                         )
        # these while loops keep asking user for user input until the user input is true to the functions
        while True:
            new_winrate = input("Enter winrate: ")
            if is_decimal_number(new_winrate):
                break
            else:
                print("That is not a valid input, Try again")

        while True:
            new_hp = input("Enter base hp: ")
            if new_hp.isdigit():
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_ad = input("Enter base ad: ")
            if new_ad.isdigit():
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_armor = input("Enter base armor: ")
            if new_armor.isdigit():
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_magicresist = input("Enter base magic resist: ")
            if new_magicresist.isdigit():
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_attackspeed = input("Enter base attack speed: ")
            if is_decimal_number(new_attackspeed):
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_attackrange = input("Enter base attack range: ")
            if new_attackrange.isdigit():
                break
            else:
                print("That is not a valid input, try again.")

        while True:
            new_movespeed = input("Enter base movespeed: ")
            if new_movespeed.isdigit():
                break
            else:
                print("That is not a valid input, try again.")
        
        # after everything checks out, then it will run the insert data function        
        insert_data(new_champion_name, new_role, new_lane, new_winrate, new_hp, new_ad, new_armor, new_magicresist, new_attackspeed, new_attackrange, new_movespeed)
    elif user_input == "d":
        # runs delete function
        # asks user what champion they want to delete
        # checks if champion exists in database and if it doesn't then the user will be sent back to the menu
        champions_name()
        delete_champion_name = input("Enter champion you would like to delete (enter nothing to go back)\n"
                                     "You: "
                                     )

        if delete_champion_name == "":
            print("\n")

        elif is_champion_real(delete_champion_name):
            delete_data(delete_champion_name)
        else:
            print("\n")
            print(f"{delete_champion_name} is not a champion in the database\nDeletion failed.\n")
            print("\n")
        

    elif user_input == "u":
        # runs update function
        # asks user which champions data they want to update and assigns a variable to that to be used in the update function
        # checks if champion exists in database and if it doesn't then the user will be sent back to the menu
        champions_name()
        which_update_champion = input("Enter the champion you would like to update (enter nothing to go back)\n"
                                      "You: "
                                        )
        is_champion_real(which_update_champion)
        if which_update_champion == "":
            print("\n")
        # when champion is in the database and user doesn't want to go back then it will ask the user which column that want to update
        elif is_champion_real(which_update_champion):
            column_name = input("Which column would you like to update\n"
                            "name, role, lane, winrate, hp, ad, armor, magicresist, attackspeed, attackrange, movespeed\n"
                            "You: "
                            )
            # asks the user for the new value and assigns a variable based on the column used in update function
            if column_name == "name":
                update_champion_name = input("Enter new champion name: ")
                update_data_name(which_update_champion, update_champion_name)
            elif column_name == "role":
                update_role = input("Enter new role\n"
                                    "assassin, mage, tank, marksmen, support, fighter\n"
                                    "You: "
                                    )
                update_data_role(which_update_champion, update_role)
            elif column_name == "lane":
                update_lane = input("Enter new lane\n"
                                    "mid, bottom, top, jungle\n"
                                    "You: "
                                    )
                update_data_lane(which_update_champion, update_lane)
            # the while loops will keep asking the user for input until the user enters a valid input
            elif column_name == "winrate":
                while True:
                    update_winrate = input("Enter new winrate: ")
                    if is_decimal_number(update_winrate):
                        update_data_winrate(which_update_champion, update_winrate)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "hp":
                while True:
                    update_hp = input("Enter new base hp: ")
                    if update_hp.isdigit():
                        update_data_hp(which_update_champion, update_hp)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "ad":
                while True:
                    update_ad = input("Enter new base ad: ")
                    if update_ad.isdigit():
                        update_data_ad(which_update_champion, update_ad)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "armor":
                while True:
                    update_armor = input("Enter new base armor: ")
                    if update_armor.isdigit():
                        update_data_armor(which_update_champion, update_armor)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "magicresist":
                while True:
                    update_magicresist = input("Enter new base magic resist: ")
                    if update_magicresist.isdigit():
                        update_data_magicresist(which_update_champion, update_magicresist)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "attackspeed":
                while True:
                    update_attackspeed = input("Enter new base attack speed: ")
                    if is_decimal_number(update_attackspeed):
                        update_data_attackspeed(which_update_champion, update_attackspeed)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "attackrange":
                while True:
                    update_attackrange = input("Enter new base attack range: ")
                    if update_attackrange.isdigit():
                        update_data_attackrange(which_update_champion, update_attackrange)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "movespeed":
                while True:
                    update_movespeed = input("Enter new base movespeed: ")
                    if update_movespeed.isdigit():
                        update_data_movespeed(which_update_champion, update_movespeed)
                        break
                    else:
                        print("That is not a valid input, Try again")
            elif column_name == "":
                pass
            else:
                print("\nThat was not a valid input\nUpdate failed.\n")
        else:
            print(f"{which_update_champion} is not a champion in the database\nTry again.")
            
    elif user_input == "":
        break
    else:
        print("\nThat was not a valid input, Try again\n")