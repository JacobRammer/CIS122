'''
CIS 122 Fall 2018 Assignment 6
Author: Jacob Rammer
Partner: None
Description: Read a number txt file and display results
'''
from cis122_assign06_shared import pad_left, pad_right
import os

label_spacing = num_spacing = 10  # How far to pad using pad() function

while True:
    line_count = comments = line_number = total = 0
    file_name = input("Enter a file name (blank to exit): ").strip()
    if len(file_name) == 0:
        break

    if os.path.exists(file_name):
        fin = open(file_name)

        for line in fin:  # Counts line in the file
            if line[0:1] == "#":  # Counts comment lines
                comments += 1
            elif line[0:1].isdigit():  # Counts lines that are integers
                line_count += 1
                total += int(line)  # Calculates the total of all integers in file
        fin.close()
        pad_right("Count:", label_spacing), pad_left(str(line_count), num_spacing)
        pad_right("Comments:", label_spacing), pad_left(str(comments), num_spacing)
        pad_right("Total:", label_spacing), pad_left(str(total), num_spacing)
        pad_right("Average:", label_spacing), pad_left(str(total / line_count), num_spacing)

    else:  # If filename does not exist. Print error and re-prompt
        print("Invalid filename: ", file_name)
