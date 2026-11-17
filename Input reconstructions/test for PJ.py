def show_menu():
    print("==== Welcome to the data base, choose one to continue ====")
    print("1. search for buildings")
    print("2. show details of the builings")
    print("3. building state check")
    print("4. Management page for all buildings")
    print("5. Exit the data base")


############################################################################

def main(): # use only a function to simplify the process when running the program
   running = True
   while running:
       show_menu()
       choice = input("Enter your choice: ")
       if choice == "1":
           Bld_number = int(input("Please enter the building number:"))
           exists_bulidings = [8, 9, 10, 20, 21, 22, 41, 43, 40]
           if Bld_number in exists_bulidings:
               print("The building number is valid. Do you want to continue? ")
               Choice_in_1 = input("Enter your choice [Y] or [N]: ")
               if Choice_in_1 == "Y":
                   return
               elif Choice_in_1 == "N":


           else:
               print("The building number is not valid.")




###########################################################################

if __name__ == '__main__':
    main()

##########################################################################
