# Task 1: Perform Basic Mathematical Operations

try:
    # Take two numbers as input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Display results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")

    # Handle division with check for zero
    if num2 != 0:
        division = num1 / num2
        print(f"Division: {division}")
    else:
        print("Division: Cannot divide by zero")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
