import random
from myModule import greeting

def get_random():
    random_num = random.randint(1, 100)
    print(f"Random: {random_num}")


def add_two_num():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    sum = num1 + num2
    print(f"Total sum: {sum}")


def display_menu():
    while True:
        print("Choose an option:")
        print("A - Run local function")
        print("B - Run function from Standard Module")
        print("C - Run function from Custom Module")
    
        choice = input("Enter your option: ").upper()

        if choice == "A":
            add_two_num()
        elif choice == "B":
            get_random()
        elif choice == "C":
            greeting()
        else:
            print("Good bye!")
            break


display_menu()