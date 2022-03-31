# description 
"""
Pycalc
2022
Daniel Chavez
A simple test python calculator

"""
# imports


# global variables



# functions
def print_menu():
    print("=======================")
    print(" PyCalc 3000")
    print("=======================")
    
    print("[1] - Sum")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")

    print("[5] - Repeat message")

    print("q - Quit")

# ask for a message
# 

# plain instructions


print_menu()
option = input("Please select an option: ")

if option != "5":
    num1 = float(input("Please provide the num 1: "))
    num2 = float(input("Please provide the num 2: "))

if option == "1":
    res = num1 + num2
    print(f"The result is: {res}")
    
# else if the option is 2, ask for 2 number and show the result of num1 - nu2 

elif option == "2":
    res = num1 - num2
    print(f"The result is: {res}")

elif option == "3":
    res = num1 * num2
    print(f"The result is: {res}")

elif option == "4":
    if num2 == 0:
        print("Don't divide by zero, you will kill us all")
    else:
        res = num1 / num2 == 0 
        print(f"The result is: {res}")

elif option == "5":
    message = input("Provide your message: ")
    times = int(input("How many times? ")) 

    for i in range(0, times):
        print(message)