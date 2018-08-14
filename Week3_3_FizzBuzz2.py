'''
WEEK 3: EXERCISE 3

Receive an integer at the input and print 'Buzz' if the number is divisible by 5.
Otherwise, print the same number as the entry.
'''

num = int(input("Entry an integer: "))

if (num % 5 == 0):
  print("Buzz")
else:
  print(num)
