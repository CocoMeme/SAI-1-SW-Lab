import random
from myModule import greet_user

def add_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def get_random_number():
    random_number = random.randint(1, 100)
    print(f"Random number: {random_number}")

def display_menu():
    while True:
        print("\nChoose an option:")
        print("A - Run local function (add two numbers)")
        print("B - Run standard module function (get random number)")
        print("C - Run custom module function (greet user)")
        print("Q - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'A':
            add_two_numbers()
        elif choice == 'B':
            get_random_number()
        elif choice == 'C':
            name = input("Enter your name: ")
            greet_user(name)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    display_menu()
