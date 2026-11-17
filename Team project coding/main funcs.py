"""
BMS - Building Management System
noted by Kevin, Yumo Qiu

This .py provides the basic logic and explanation for our team project.
All classes and variables should obey the rules listed in the main drive.

(f) functions that have been defined
(v) variables that have been defined
(c) classes that have been defined
(l) lists created to temporarily store data that can be tested
filling：Shuaiye Wang, Yuyang Jin.
testing: Qiujie Lv
"""

# (v) + (l) building numbers that exist in the database
EXI_BLD = [8, 9, 10, 20, 21, 22, 40, 41, 43]

# (v) the choices offered by the menu and handed to cho_log
CHOICES = ["1", "2", "3", "4", "5"]

def show_menu():
    print("==== Welcome to the data base, choose one to continue ====")
    print("1. search for buildings")
    print("2. show details of the buildings")
    print("3. building state check")
    print("4. Management page for all buildings")
    print("5. Exit the data base")

# choice 1
def search_building():
    raw = input("Please enter the building number: ").strip()
    # Statement: the "strip()" is not included in our module. we learnt it from the Internet and of course the reference is provided.
    # The function of ".strip()" is to delete the unnoticed blanks.  e.g." 1" and "1" may be differently defined
    # the former is wrong/invalid and the second is recognized. using ".strip()"can make them all runnable if the mamager
    # types in a blank by mistake. This is a complement of C language.
    try:
        bld_num = int(raw)
    except ValueError:
        print("This is not a number.")
        return # this decides when the number is not vaild, run again.

    if bld_num not in EXI_BLD:
        print("!Building", bld_num, "does not exist.")
        return # this decides if the number is not in the list, run again.

    print("Building", bld_num, "is valid.")
    answer = input("Do you want to continue? [Y/N]: ").strip().upper() # the "upper()" is still learnt from the Internet
    # it can include both the uppercase and lowercase.and if you type in an lowercase, the function will help convert
    # it into a valid uppercase
    if answer == "Y":
        return
    elif answer == "N":
        print("Returning to the main menu.")
        return
    else:
        print("Only Y or N is accepted.")

# choice 2
def show_details():
    for bld_num in EXI_BLD:
        print("  - Building", bld_num, ": details not implemented yet")

# choice 3
def state_check():
    print("Building state check: not implemented yet")


def management_page():
    """(f) choice 4: management page for all buildings."""
    print("Management page: not implemented yet")


def cho_log(choices):
    """(f) main logic: show the menu, read a choice, react to it."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice not in choices:
            print("[!] Invalid choice, please enter 1-5.")
            continue

        if choice == "1":
            search_building()
        elif choice == "2":
            show_details()
        elif choice == "3":
            state_check()
        elif choice == "4":
            management_page()
        elif choice == "5":
            print("Goodbye.")
            break

def main_page():
    print("BMS initializing ...")
    # this needs to be filled.
    cho_log(CHOICES)


if __name__ == "__main__":
    main_page()
 # this needs to be filled.