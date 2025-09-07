# factorial_function.py

def factorial(n):
    """Function to calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
