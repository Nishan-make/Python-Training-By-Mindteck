# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file name contains the word "Python".
# - Print the file name if the word is found

import glob
import re

# Find all .txt files in the current folder
txt_files = glob.glob("*.txt")

# Check each file for the word "Python"
for filename in txt_files:
    with open(filename, 'r') as file:
        content = file.read()
        if re.search(r'\bPython\b', content):
            print(f"Found 'Python' in: {filename}")

# ============================================================================

# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 

# List all files in the current directory
all_files = glob.glob("*")

# Match file names using re.match
for file in all_files:
    if re.match(r'^data_.*\.csv$', file):
        print(f"CSV File matched: {file}")

# =============================================================================

# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

# Sample list of phone numbers
phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987) 654-3210",
    "(123)456-7890",
    "(000) 000-0000"
]

# Regex pattern: (xxx) xxx-xxxx
pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')

# Validate and print only correctly formatted phone numbers
for number in phone_numbers:
    if pattern.match(number):
        print(f"Valid phone number: {number}")
