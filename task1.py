def factorial(n):
    """
    Calculate factorial using recursion.

    Parameters:
    n (int): A non-negative integer

    Returns:
    int or str: Factorial of n or error message
    """
    
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)   # 🔥 recursion happens here


# User input
num = int(input("Enter a number: "))

# Output
print("Factorial of", num, "is:", factorial(num))
