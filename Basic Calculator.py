# This Python3 program is to create a simple calculator.
# It takes two numbers and the mathematical operation as input from the user.
# Then performs the operation for the two numbers provided.

# Create a function for adding two numbers
def add(x, y):
    return x + y

# Create a function for subtracting two numbers
def subtract(x,y):
    return x - y

# Create a function for multiplying two numbers
def multiply(x,y):
    return x * y

# Create a function for dividing1
# two numbers
def divide(x,y):
    return x / y

# Print the operator choices.
print("This is a Simple Calculator")
print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take the operation choice from the user.
choice = int(input("Enter the choice (1/2/3/4)"))

# Take the numbers as input from user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Based on the user input, perform the mathematical operation.
if choice == 1:
    print("The sum of ",num1," and ",num2," is: ",add(num1,num2))
elif choice == 2:
    print("The difference between ", num1, " and ", num2, " is: ", subtract(num1, num2))
elif choice == 3:
    print("The product of ", num1, " and ", num2, " is: ", multiply(num1, num2))
elif choice == 4:
    print("The quotient of ", num1, " and ", num2, " is: ", divide(num1, num2))
else:
    print("Please enter a valid input")
