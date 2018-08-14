'''
WEEK 2: EXERCISE 2

Make a program in Python that receives four grades, calculates and prints the
arithmetic mean.

Example:

Data entry: "Entry the first grade: 4", "Entry the second grade: 5"
            "Entry the third grade: 6", "Entry the fourth grade: 7"
Data output: "The arithmetic mean is 5.5"
'''

n1 = input("Entry the first grade: ")
n2 = input("Entry the second grade: ")
n3 = input("Entry the third grade: ")
n4 = input("Entry the fourth grade: ")
mean = (float(n1) + float(n2) + float(n3) + float(n4))/4
print("The arithmetic mean is", mean)
