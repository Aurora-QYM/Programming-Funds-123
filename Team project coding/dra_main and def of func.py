"""(noted by Kevin , Yumo Qiu
This .py is used to provide a basic logic and explanation towards our team project
All the classes and variables should obey the rules listed in the main drive
We shall build a Building management system, in abbreviation BMS
the list may provide some reference both for group members and also graders
    (f)indicates functions that have been defined
    (v)indicates variables that have been defined
    (c)indicates classes that have been defined
    (l)indicates lists that have been created to temporarily store the data that can be tested

show_menu()............(f)demonstrate the options
main_page..............(f)visualize the page and keep running
cho_log(choices).......(f)main logic for guiding the mamagers into each choice and react to their choices
choices................(v)the mamagers' choices included and returned to cho_log


"""
############################################################################################
import tkinter as tk

def show_menu():
    print("==== Welcome to the data base, choose one to continue ====")
    print("1. search for buildings")
    print("2. show details of the builings")
    print("3. building state check")
    print("4. Management page for all buildings")
    print("5. Exit the data base")

def main_page:

def cho_log(choice):
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            Bld_num = int(input("Please enter the building number:"))
            exi_bld = [8, 9, 10, 20, 21, 22, 41, 43, 40]
            if Bld_num in exi_bld:
                print("The building number is valid. Do you want to continue? ")
                Choice_in_1 = int(input("Enter your choice [Y] or [N]: "))
                if Choice_in_1 == "Y":
                    return
                elif Choice_in_1 == "N":

