# this program replaces string in a input file and saves it

import os

# read inputs
print("enter input file:")
infile = input()

# check if input file is real
if not os.path.isfile(infile):
    print("Input file does not exist or is not a file.")
    exit()

print("enter string to be replaced:")
before = input()
print("enter string to replace with:")
after = input()

print("New file name:")
newfile = input()

# check if outfile can be written
if os.path.isfile(newfile):
    print("New file already exists. Please choose a different name.")
    exit()

# read the input file
try:
    with open(infile) as f:
        filecontent = f.read()
except Exception as e:
    print(f"Error reading input file: {e}")
    exit()

# replace the string in the file content
filecontent = filecontent.replace(before, after)

# write the modified content to the new file
try:
    with open(newfile, 'w') as f:
        f.write(filecontent)
except Exception as e:
    print(f"Error writing to new file: {e}")
    exit()