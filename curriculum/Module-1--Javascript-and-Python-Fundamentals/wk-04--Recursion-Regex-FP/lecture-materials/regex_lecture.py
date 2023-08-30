import re

regular_expression = r'sting'
my_string = "string string string"
# value = 2
# my_string = r'\t{value} \n is a value'
# print(my_string)

# print(re.search(regular_expression, my_string))
# print(re.findall(regular_expression, my_string))
# print(re.match(regular_expression, my_string))


## a .. z, A .. Z, 0 - 9 - match exactly
## ^ . $ * + { } [ ] \ | ( ) - special characters, which are interpreted by the re library

## . matches any character except the newline \n

# regex_pattern = r"str.ng"
# my_new_string = "strng strung str\nng straung"
# print(re.findall(regex_pattern, my_new_string))

## \w any letter, digit or underscore == [a-zA-Z0-9_]

# regex_pattern_2 = r"\w\wfoo"
# my_new_string_3 = "foo 1foo _foo afoo cfoo abfoo"
# print(re.findall(regex_pattern_2, my_new_string_3))

## \W not any letter digit or underscore
## \s any whitespace character
## \t \n \r, tab, newline, return

## \d matches any decimal digit 0-9 = [0-9]
## ^ match the start of string

# regex_pattern_3 = r"^[bc]at"
# my_new_string_4 = "cat \nbat \nat \nsat"
# print(re.findall(regex_pattern_3, my_new_string_4, re.MULTILINE))

## $ - match the end of the string
# regex_pattern_3 = r"sat$"
# my_new_string_4 = "cat \nbat \nat \n sat"
# print(re.findall(regex_pattern_3, my_new_string_4, re.MULTILINE))

## \. to match a period, \ inhibits the specialness of the .

## * zero or more occurences of the pattern to the left of the *
# regex_pattern = r"a*"
# my_new_string = "bt bat baat baaat baaaat"
# print(re.findall(regex_pattern, my_new_string))

## + matches one or more occurences of the pattern to the left
# regex_pattern = r"a+"
# my_new_string = "bt bat baat baaat baaaat"
# print(re.findall(regex_pattern, my_new_string))

## ? matches zero or one occurences of the pattern to the left

## simple email address matching regular expression
##  @ in middle
## one or more number of letters, numbers, and underscores followed by the @ symbol, one or more number of letters, numbers and underscores
## followed by a dot and exactly 3 lowercase letters

# email_regex = r"\w+@\w+\.[a-z][a-z][a-z]"
# string_of_things = "john@john.comf j27@j27.com j54$@j54.com hello 123 any street"
# print(re.findall(email_regex, string_of_things))

## 1234567890
## (123)456-7890
## 123-456-7890

phone_number_regex = r"[\(]?(\d{3})[\)]?-?(\d{3})[-]?(\d{4})"
phone_number_test = "7778675309"
print(re.findall(phone_number_regex, phone_number_test))