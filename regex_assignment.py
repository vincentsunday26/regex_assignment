# Task 1: Name Verification

import re
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    # Define the regex pattern for a valid name
    pattern = re.compile(r'^[A-Z][a-z]*([ ][A-Z][a-z]*)*$')
    
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")