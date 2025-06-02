import math
import random

# Basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to calculate factorial
def factorial(num):
    return math.factorial(num)

# Perform arithmetic operation on a list
def operate_on_list(operation):
    valid_operations = {'add', 'subtract', 'multiply', 'divide'}
    if operation not in valid_operations:
        print(f"Error! Invalid operation '{operation}'. Choose from add, subtract, multiply, divide.")
        return

    numbers = input("Enter numbers separated by spaces: ").split()
    try:
        numbers = [float(num) for num in numbers]
    except ValueError:
        print("Error! Non-numeric input.")
        return

    if len(numbers) < 2:
        print("Error! At least two numbers are required.")
        return

    result = numbers[0]
    for num in numbers[1:]:
        if operation == 'add':
            result = add(result, num)
        elif operation == 'subtract':
            result = subtract(result, num)
        elif operation == 'multiply':
            result = multiply(result, num)
        elif operation == 'divide':
            if num == 0:
                print("Warning! Division by zero skipped.")
                continue
            result = divide(result, num)

    print("Result:", round(result, 2))

# Helper function to get operation symbol for history
def get_op_symbol(choice):
    return {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/',
        '5': '%',
        '6': '**'
    }.get(choice, 'op')

# Main interaction function
def main():
    print("Welcome to MyCalculator!")
    history = []

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Square Root")
        print("8. Check Prime")
        print("9. Find Factorial")
        print("10. Generate Random Number")
        print("11. Operate on a List")
        print("12. View History")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        try:
            if choice in ('1', '2', '3', '4', '5', '6'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    if num2 == 0:
                        print("Error! Division by zero.")
                        continue
                    result = divide(num1, num2)
                elif choice == '5':
                    result = modulus(num1, num2)
                elif choice == '6':
                    result = exponent(num1, num2)

                print("Result:", round(result, 2))
                op_symbol = get_op_symbol(choice)
                history.append(f"{num1} {op_symbol} {num2} = {round(result, 2)}")

            elif choice == '7':
                num = float(input("Enter number to find square root: "))
                if num < 0:
                    print("Error! Square root of negative number.")
                    continue
                result = square_root(num)
                print("Result:", round(result, 2))
                history.append(f"sqrt({num}) = {round(result, 2)}")

            elif choice == '8':
                num_input = input("Enter a positive integer to check if it's prime: ")
                if not num_input.isdigit() or int(num_input) <= 0:
                    print("Error! Please enter a positive integer.")
                    continue
                num = int(num_input)
                result = is_prime(num)
                msg = f"{num} is {'a prime' if result else 'not a prime'} number."
                print(msg)
                history.append(msg)

            elif choice == '9':
                num_input = input("Enter a non-negative integer to find its factorial: ")
                if not num_input.isdigit():
                    print("Error! Please enter a non-negative integer.")
                    continue
                num = int(num_input)
                result = factorial(num)
                print("Factorial of", num, "is", result)
                history.append(f"{num}! = {result}")

            elif choice == '10':
                result = random.randint(1, 100)
                print("Random number:", result)
                history.append(f"Random number = {result}")

            elif choice == '11':
                operation = input("Enter list operation (add / subtract / multiply / divide): ").lower()
                operate_on_list(operation)

            elif choice == '12':
                print("\nHistory:")
                if history:
                    for entry in history:
                        print(entry)
                else:
                    print("No operations performed yet.")

            elif choice == '13':
                print("Exiting the calculator. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 13.")

        except ValueError:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()
