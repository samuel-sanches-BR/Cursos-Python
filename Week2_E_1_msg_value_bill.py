'''
WEEK 2: EXTRA EXERCISE 1

A credit card company sends your bills by email with the following message:
"Hello, Jorge
Your bill due on January 9th, worth R$ 350.00 is closed."

Write a program that receives (keystroke input) the customer name, expiration date,
month of expiration, and invoice amount, and print (data output) the message with
the received data in the same format as the message above. Note that the program
prints the output on two different lines. Note also that because no calculations
are required, the value does not need to be converted to number, it can be treated as text.
'''

clientname = input("Entry the client's name: ")
expirationdate = input("Entry the expiration date: ")
expirationmonth = input("Entry the expiration month: ")
value = input("Entry the bill's value: ")
print("Hello,", clientname)
print("Your bill due on",expirationmonth, expirationdate,", worth R$",value,"is closed.")
