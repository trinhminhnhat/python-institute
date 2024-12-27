# 4.3.1.16 LAB: Sorted character frequency histogram
from os import strerror

def generate_histogram(file_name):
    try:
        # Read the content of the input file
        with open(file_name, 'r') as file:
            content = file.read()

        # Initialize a dictionary to count letter occurrences
        histogram = {}
        for char in content:
            if char.isalpha():  # Count only Latin letters
                char = char.lower()
                histogram[char] = histogram.get(char, 0) + 1

        # Sort the histogram by frequency (descending) using a lambda function
        sorted_histogram = sorted(histogram.items(), key=lambda item: item[1], reverse=True)

        # Prepare the output file name
        output_file_name = file_name + '.hist'

        # Write the histogram to the output file
        with open(output_file_name, 'w') as output_file:
            for char, count in sorted_histogram:
                output_file.write(f"{char} -> {count}\n")

        print(f"Histogram written to: {output_file_name}")
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

# Example usage
input_file = "./Certified Associate Python Programmer (PCAP)/labs/sorted-character-frequency-histogram/samplefile.txt"  # Replace with your input file
generate_histogram(input_file)
