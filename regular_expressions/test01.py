import re

# Scenario 1 >> \s
print( re.search(r'Not a\sregular character', 'Not a regular character').group() )

# Scenario 2 >> \r
print( re.search(r'Just a \regular character', 'Just a \regular character').group() )

# Scenario 3 >> \\
print( re.search(r'Just a \\sregular character', 'Just a \sregular character').group() )


# ^ - A caret. Matches the start of the string.
print( re.search(r'^Eat', "Eat cake!").group() )

# print( re.search(r'^eat', "Let's eat cake!").group() )
# ^^^ Error 
