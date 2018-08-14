'''
WEEK 3: EXERCISE 4

Receive an integer at the input and print 'FizzBuzz' if the number is divisible by 3 and 5.
Otherwise, print the same number as the entry.
'''

num = int(input("Entry an integer: "))

if (num % 3 == 0 and num % 5 == 0):
  print("FizzBuzz")
else:
  print(num)
