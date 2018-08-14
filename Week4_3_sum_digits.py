'''
WEEK 4: EXERCISE 3

Write a program that receives an integer, calculate and print the sum of the number's digits.
'''

print("Sum of the digits of an integer!")

numberEntry = int(input("Digite um número inteiro: "))

suma = 0

while numberEntry != 0:
    dig = numberEntry % 10
    suma = suma + dig
    numberEntry = numberEntry // 10

print()
