# Practice 4: Count the number of lines in a file

import os

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        total_lines = len(lines)
        non_empty_lines = sum(1 for line in lines if line.strip())
        empty_lines = total_lines - non_empty_lines

        print(f"File: '{filename}'")
        print(f"  Total lines      : {total_lines}")
        print(f"  Non-empty lines  : {non_empty_lines}")
        print(f"  Empty lines      : {empty_lines}")
        return total_lines

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
        return 0


def count_words_and_chars(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        words = len(content.split())
        chars = len(content)
        chars_no_space = len(content.replace(" ", "").replace("\n", ""))

        print(f"\nExtra stats for '{filename}':")
        print(f"  Word count             : {words}")
        print(f"  Total characters       : {chars}")
        print(f"  Characters (no spaces) : {chars_no_space}")

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")


# Create a sample file to analyze
sample_file = "sample_text.txt"
with open(sample_file, "w") as f:
    f.write("Python is a powerful programming language.\n")
    f.write("It is easy to learn and fun to use.\n")
    f.write("\n")
    f.write("File handling allows us to read and write data.\n")
    f.write("JSON makes data storage structured and readable.\n")
    f.write("Together, they form the backbone of data persistence.\n")

print("=" * 40)
print("       FILE STATISTICS ANALYZER")
print("=" * 40)
count_lines(sample_file)
count_words_and_chars(sample_file)
