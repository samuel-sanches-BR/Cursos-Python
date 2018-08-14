'''
WEEK 3: EXERCISE 2

Receive an integer at the input and print 'Fizz' if the number is divisible by 3.
Otherwise, print the same number as the one given on the entry.
'''

num = int(input("Entry an integer: "))

if (num % 3 == 0):
  print("Fizz")
else:
  print(num)
