# 4.3.1.17 LAB: Evaluating students' results
from os import strerror

# Define custom exceptions
class FileError(Exception):
    """Base class for file-related errors."""
    pass

class BadLineError(FileError):
    """Raised when a line in the file has an incorrect format."""
    def __init__(self, line):
        super().__init__(f"Bad line detected: {line}")

class EmptyFileError(FileError):
    """Raised when the file is empty."""
    def __init__(self):
        super().__init__("The file is empty.")

def process_file(file_name):
    try:
        # Read the file content
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Check if the file is empty
        if not lines:
            raise EmptyFileError()

        # Initialize a dictionary to store student data
        student_scores = {}

        # Process each line
        for line in lines:
            line = line.strip()
            parts = line.split()
            if len(parts) != 3:  # Expect 3 elements per line
                raise BadLineError(line)

            # Extract data
            first_name, last_name, score = parts
            try:
                score = float(score)
            except ValueError:
                raise BadLineError(line)

            # Combine first and last names as key
            full_name = f"{first_name} {last_name}"
            student_scores[full_name] = student_scores.get(full_name, 0) + score

        # Sort and print the results
        for student, total_score in sorted(student_scores.items()):
            print(f"{student}\t{total_score}")

    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))
    except FileError as e:
        print("Error:", e)

# Ask the user for the file name
file_name = input("Enter the name of Prof. Jekyll's file: ")
process_file(file_name)
