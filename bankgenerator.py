import sys
import os

# this will check to make sure that the user
# is inputing the write syntax
# the correct syntax is:
# python bankgenerator.py text_file.txt [min] [max]
if len(sys.argv) < 4:
    print("""
          The correct syntax is as follows:
          python bankgenerator.py [textfile.txt] [minchar] [maxchar]
          """)
    sys.exit(1)


# Assiging variables from user input
text_file = sys.argv[1]
# check to make sure minchar and maxchar are integers
try:
    minchar = int(sys.argv[2])
    maxchar = int(sys.argv[3])
except ValueError:
    print("Error: minchar and maxchar must be integers")
    sys.exit(1)
# check to make sure minchar is less than maxchar
if minchar > maxchar:
    print("Error, minimum character must be less than maximum character")
    sys.exit(1)
# Check to see if text_file exists
if not os.path.exists(text_file):
    print(f"Error: the file '{text_file}' does not exist.")
    sys.exit(1)


# For loop that iterates through text file
# and adds words in the range to a new list
with open(text_file, encoding="utf-8") as big_list:
    in_range_list = []
    for word in big_list:
        if minchar <= len(word.strip()) <= maxchar:
            in_range_list.append(word.strip())

# the next bit of code checks to see if 
# an output file with the name wordbank.txt already 
# exists, and if it does, dynamically name the new file.
base_name = "wordbank"
ext = ".txt"
filename = base_name + ext
counter = 1
while os.path.exists(filename):
    filename = f"{base_name}({counter}){ext}"
    counter += 1
# For Loop that iterates through in_range_list
# and adds it to a new text file, thus creating
# the required word bank.
with open(filename, "w", encoding="utf-8") as wordbank:
    for word in in_range_list:
        wordbank.write(word + "\n")
    print(f"{filename} has been created at {os.path.abspath(filename)}")
    print(f"{len(in_range_list)} words were added to {filename}.")