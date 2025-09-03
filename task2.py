# Task 2: Create a Personalized Greeting

# Take first and last name as input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenate into full name
full_name = first_name + " " + last_name

# Print personalized greeting
print(f"Hello, {full_name}! Welcome to the Python program.")
