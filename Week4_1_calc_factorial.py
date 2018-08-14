'''
WEEK 4: EXERCISE 1

Write a program that receives a natural number 'n' and prints n!.
'''

num = int(input("Entry the number n: "))
fat = 1
n = num

while (n > 0):
    fat = fat * n
    n = n - 1

if (num == 0):
    print("1")
else:
    print(fat)
