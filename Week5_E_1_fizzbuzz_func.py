'''
WEEK 5: EXTRA EXERCISE 1

Write a function 'fizzbuzz' that receive an integer and return 'Fizz' if the number
is divisible by 3 and not by 5, 'Buzz' if the number is divisible by 5 and not by 3
and 'FizzBuzz' if the number are divisible by 3 and 5.
'''

def fizzbuzz(n):

    num = int(n)
    
    if (num % 3 == 0 and num % 5 != 0):
        return 'Fizz'
    elif (num % 5 == 0 and num % 3 != 0):
        return 'Buzz'
    elif (num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 != 0 and num % 5 != 0):
        return num
