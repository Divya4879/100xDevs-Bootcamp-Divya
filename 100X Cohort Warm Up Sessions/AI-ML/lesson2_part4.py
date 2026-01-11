# Accepting Arguments

# import sys  # import  statements- ideally the first line(s) in the program

# # terminal- py lesson2_part3.py Divya 20 Dev
# print(sys.argv)  # ['lesson2_part3.py', 'Divya', '20', 'Dev']

# name = sys.argv[1]
# print(f"Hello dear {name}")


import argparse

parser = argparse.ArgumentParser(
    description="Just a test for now dear, idk what it does yet"
)

parser.add_argument("-c", "--color", metavar="color", required= True, choices={"purple", "blue"}, help= "the color to search for")

args = parser.parse_args()

print(args.color)  # use py lesson2_part4.py  -c red on terminal- output is red.

# after adding choices, can only chose  from the options there, no other color will be accepted.