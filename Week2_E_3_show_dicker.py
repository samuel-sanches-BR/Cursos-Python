'''
WEEK 2: EXTRA EXERCISE 3

Make a program in Python that obtains an integer and prints its dickers number.
'''

numint = input("Entry an integer: ")
dicker = (int(numint) % 100) // 10
print("The dickers digit is", dicker)
