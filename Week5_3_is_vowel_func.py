'''
WEEK 5: EXERCISE 3

Write the function 'vowel' that receives one character as parameter and returns
'True' if is a vowel or 'False' if is a consonant.
'''

def vowel(a):

    if (a == "a" or a == "A" or a == "e" or a == "E" or a == "i" or a == "I" or a == "o"
        or a == "O" or a == "U" or a == "u" or a == "U"):
        return True
    else:
        return False
