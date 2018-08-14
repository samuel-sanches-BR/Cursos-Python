'''
WEEK 2: EXERCISE 1

Write the function 'capital(phrase)' which receives a phrase and returns
a string with the capital letters.
'''

def capital(phrase):
    phrase = phrase.strip()
    let = ''
    for x in range(0, len(phrase)):
        if (ord(phrase[x]) >= 65 and ord(phrase[x]) <= 90):
            let = let + chr(ord(phrase[x]))

    return let
