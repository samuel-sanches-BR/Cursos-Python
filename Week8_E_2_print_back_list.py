'''
WEEK 8: EXTRA EXERCISE 2

As requested in the first video lesson of this week, write a program that receives
a sequence of integers and print all the values in reverse order. The sequence
always ends with the number 0. Note that 0 (ZERO) should not be part of the sequence.
'''

x = int(input("Entry a number: "))
list1=[]

while (x != 0):
    list1.append(x)
    x = int(input("Entry a number: "))

for x in list1[len(list1)::-1]:
    print(x)
        
