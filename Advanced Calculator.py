# This Python3 program is to create a calculator.
# It takes a mathematical equation from the user and returns the result of the equation.
# It will not quit until the user explicitly specifies the program to do so.

# Import Regex library.
import re

print("Welcome to the Calculator.")
print("Type 'quit' to exit\n")

previous = 0
run = True


def solveEquation():
    global run                                      # To modify the variable run within this function.
    global previous                                 # To modify the variable previous within this function.
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye !!!")
        run = False
    elif equation == 'new':
        previous = 0
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)                   # Inbuilt function to solve a mathematical equation.
        else:
            previous = eval(str(previous) + equation)  # Evaluate the previous result and the new equation.


while run:
    solveEquation()
