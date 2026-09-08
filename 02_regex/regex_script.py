# Regex training script
# Purpose: practice core regex patterns and behaviors in Python's re module.

import re


# --------------------------------------------------
# BLOCK 1: Basic email pattern with capturing groups
# --------------------------------------------------

# Compile a regex pattern that captures:
#  - group(1): the username part before '@' (letters, digits, underscore)
#  - group(2): the domain part after '@' (like 'company.com')
pattern = re.compile(r'(\w+)@(\w+\.\w+)')

# Search for the first match of this pattern in the given string
match = pattern.search('contact@company.com')

if match:
    print(match.group(0))  # Full match: 'contact@company.com'
    print(match.group(1))  # Username: 'contact'
    print(match.group(2))  # Domain: 'company.com'


# --------------------------------------------------
# BLOCK 2: Optional character with '?'
# --------------------------------------------------

# 'colou?r' means:
#  - 'color'  (without 'u')
#  - 'colour' (with 'u')
# The 'u?' makes the 'u' optional.
pattern = re.compile(r'colou?r')

print(pattern.search('color').group())   # Matches 'color'
print(pattern.search('colour').group())  # Matches 'colour'


# --------------------------------------------------
# BLOCK 3: Extract multiple emails from text
# --------------------------------------------------

text = "Emails: info@example.com, support@example.com"

# Regex explanation:
#  - \b                : word boundary (start/end of a word)
#  - [\w.%+]+          : one or more word chars, '.', '%', '+' (username part)
#  - @                 : literal '@'
#  - [\w-]+            : one or more word chars or '-' (domain name)
#  - \.                : literal dot '.'
#  - [a-zA-Z]{2,}      : 2 or more letters (TLD like 'com', 'io', 'info')
#  - \b                : word boundary
emails = re.findall(r'\b[\w.%+]+@[\w-]+\.[a-zA-Z]{2,}\b', text)

print(emails)  # ['info@example.com', 'support@example.com']


# --------------------------------------------------
# BLOCK 4: Character class for vowels
# --------------------------------------------------

# [aeiou] means "any one character that is a, e, i, o, or u"
pattern = re.compile(r'[aeiou]')

# findall returns all matching characters in order
print(pattern.findall('hello world'))  # ['e', 'o', 'o']


# --------------------------------------------------
# BLOCK 5: Simple phone number validation
# --------------------------------------------------

phone = "123-456-789"

# Regex explanation:
#  - ^           : start of string
#  - \d{3}       : exactly 3 digits
#  - -           : literal hyphen
#  - \d{3}       : exactly 3 digits
#  - -           : literal hyphen
#  - \d{4}       : exactly 4 digits
#  - $           : end of string
if re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
    print("Valid")
else:
    print("Invalid")  # This will print "Invalid" for "123-456-789"


# --------------------------------------------------
# BLOCK 6: Greedy vs non-greedy quantifiers
# --------------------------------------------------

text = "<p>First</p><p>Second</p>"

# Greedy: '.*' will match as much as possible
greedy = re.compile(r'<p>.*</p>')

# Non-greedy: '.*?' will match as little as possible
non_greedy = re.compile(r'<p>.*?</p>')

print(greedy.findall(text))      # ['<p>First</p><p>Second</p>']
print(non_greedy.findall(text))  # ['<p>First</p>', '<p>Second</p>']


# --------------------------------------------------
# BLOCK 7: Case-insensitive substitution
# --------------------------------------------------

text = "Hello WORLD"

# re.sub replaces 'world' (case-insensitive) with 'Python'
