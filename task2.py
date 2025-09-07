# math_module_calculations.py

import math

# Main program
if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        
        sqrt_val = math.sqrt(num)
        log_val = math.log(num)   # natural log (base e)
        sine_val = math.sin(num)  # sine in radians

        print(f"Square root: {sqrt_val}")
        print(f"Logarithm: {log_val}")
        print(f"Sine: {sine_val}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
