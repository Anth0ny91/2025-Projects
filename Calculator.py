from colorama import Fore, Style, init
import time
import os
import sys

init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print(Fore.CYAN + "="*50)
print(Fore.YELLOW + "         WELCOME TO CMD CALCULATOR")
print(Fore.CYAN + "="*50 + Style.RESET_ALL)

print("Loading", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.4)
print("\n")
time.sleep(3)
clear_console()
print(r"""
  ____        _            _       _             
 |  _ \  __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | | | |/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |_| | (_| | | (__| |_| | | (_| | || (_) | |   
 |____/ \__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        Welcome to my CMD Calculator
""")

#Functions
def add_function(x, y):
    return x + y

def sub_function(x, y):
    return x - y

def div_function(x, y):
    return x / y

def multi_function(x, y):
    return x * y

while True:
    try:
        print("Choose an operation:")
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")

        user_choice = input("Enter 1, 2, 3, or 4: ")

        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))

        if user_choice == '1':
            result = add_function(x, y)
            print(f"The sum is {result}!")
        elif user_choice == '2':
            result = sub_function(x, y)
            print(f"The difference is {result}!")
        elif user_choice == '3':
            result = multi_function(x, y)
            print(f"The product is {result}!")
        elif user_choice == '4':
            if y == 0:
                print("Cannot divide by zero.")
                continue
            result = div_function(x, y)
            print(f"The quotient is {result}!")
        else:
            print("Invalid choice. Try again.")
            continue

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    # Ask if user wants to try again
    restart = input("Try again? Y/N: ").lower()
    if restart != "y":
        print("Thanks for using the calculator!")
        print("Goodbye!")
        time.sleep(1)
        clear_console()
        sys.exit()


