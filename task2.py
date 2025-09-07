# write_append_file.py

def write_and_append(filename):
    """Writes user input to file, appends more data, then displays final content"""
    try:
        # Step 1: Write to file
        text = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(text + "\n")
        print(f"Data successfully written to {filename}.")

        # Step 2: Append to file
        more_text = input("Enter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(more_text + "\n")
        print("Data successfully appended.")

        # Step 3: Read and display file content
        print(f"\nFinal content of {filename}:")
        with open(filename, 'r') as file:
            print(file.read())
    except Exception as e:
        print("An error occurred:", e)

# Main program
if __name__ == "__main__":
    write_and_append("output.txt")
