import math

def calculate_values(num):
    """
    Calculate square root, logarithm, and sine.

    Parameters:
    num (float): Input number

    Returns:
    tuple: (sqrt, log, sin) or error message
    """
    
    if num < 0:
        return "Error: Logarithm is not defined for negative numbers"

    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sin_val = math.sin(num)

    return sqrt_val, log_val, sin_val


# User input
num = float(input("Enter a number: "))

result = calculate_values(num)

# Output
if isinstance(result, str):
    print(result)
else:
    print("Square root:", result[0])
    print("Logarithm:", result[1])
    print("Sine:", result[2])
