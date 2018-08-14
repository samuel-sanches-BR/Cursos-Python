'''
WEEK 2: EXTRA EXERCISE 2

Rewrite the program 'contaSegundos' to print the number of days, that is, make a
program in Python that, given the amount of seconds, "break" this value in days,
hours, minutes and seconds. The output should be in the format: a days, b hours,
c minutes, and d seconds. Be careful with the format! Too many spaces, missing
commas, or other differences are considered errors!
'''

seconds_str = input("Please, entry with the number of seconds which you want to convert: ")
total_segs = int(seconds_str)

days = total_segs // 86400
segs_rest1 = total_segs % 86400

hours = segs_rest1 // 3600
segs_rest = total_segs % 3600

minutes = segs_rest // 60
segs_rest_final = segs_rest % 60

print(days,"days,",hours,"hours,",minutes,"minutes and",segs_rest_final,"seconds.")
