'''
WEEK 2: EXTRA EXERCISE 1

Write the function 'count_letters(phrase, count = "vowel")',
which receives as first parameter a string with a phrase and as second
another string (must be optional). When the second is "vowel" the function
should return the number of vowels on the phrase and when is "consonant"
the function should return the number of consonants on the phrase.
If none is passed to the second parameter, the default is "vowel"
'''

def count_letters(phrase, count = "vowel"):
    vowe = ['a','e','i','o','u']
    conso = ['b','c','d','f','g','h','j','k','l','m','n',
             'p','q','r','s','t','v','w','x','z','k','y']
    num = 0
    phrase = phrase.lower()
    if (count == "vowel"):
        for x in vowe:
            num = num + phrase.count(x)
    elif (count == "consonant"):
        for x in conso:
            num = num + phrase.count(x)
    return num
