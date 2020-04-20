# Given a name, return a string with the message:
# One for X, one for me.

# Where X is the given name.
# However, if the name is missing, return the string:
# One for you, one for me.

# must handle exceptions like if name is missing give you
# input must be a string and maybe ensure first letter is capitialized(?)
import re 

'''Good Inputs'''
input = "Francis"
# input = "Bill"

'''Bad inputs'''
# input = 4
# input = .23

'''Edge Cases'''
# input = '.'
# input = ''


if type(input) != str: #ensure its a string
    print("input must be a string")
if input == '':
    print("One for you, one for me.")
else: 
    print('One for {x}, one for me.'.format(x=input))

    