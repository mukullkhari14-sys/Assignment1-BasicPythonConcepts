# read_file_handle_errors.py

def read_file(filename):
    """Reads and prints file content line by line"""
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Main program
if __name__ == "__main__":
    read_file("sample.txt")
