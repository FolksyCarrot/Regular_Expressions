import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
# The regex above: [a-zA-Z0-9] means to check any alphabetic character, lower case or uppercase, and to check for integers from 0-9. The '@' means to match that symbol. The '+' indicates to check for multiple, that is to check until a character that is not an alphabetic or integer occurs.
# The '\.' means a literal period, such as would be found in a proper email. The () is for matching the words and the '|' essentially means "or"
user_input = input("Enter your email address to see if it's valid!: ")
if(re.search(pattern, user_input)):
    print("Valid email")
else:
    print("invalid")
    
    
strs = str(input("enter a string!: "))
match = r'\bhello\b'
#\b means to match but where the word or letter is not followed or preceeded by another word-character
#r.search is provided 2 parameters, 1. it takes what its supposed to match, 2. It takes where you want to search for the match
if(re.search(match,strs)):
    print ("Found Yay!")
else:
    print("not found")
    
#The split is provided 2 parameter, pattern and string. The '\s' means to match whitespace, which is where it realizes to split it.    
    
string = str(input("Enter a sentence to see it split: "))
outcome = re.split('\s', string)
print(outcome)
