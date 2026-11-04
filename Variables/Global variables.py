import time
def do_greeting(name):
    print(f"\033[1;36mGood morning , {name}\033[0m")
    print(f"\033[4;33mGood morning , {name}\033[0m")

do_greeting('Dave')
do_greeting('Kevin')


