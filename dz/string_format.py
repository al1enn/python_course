# 1-primer
#!1-jol
"""
str = input("Введите строку:")
str = str.lower().capitalize()
new_str = ""
counter = 0
for char in str:
    if counter == (len(str)-1):
        char = char.upper()
    new_str += char
    counter += 1
print(new_str)
"""
#!2-jol
"""
str = input("Введите строку:")
str = str.lower().capitalize()
last_char_index = len(str)-1
last_char = str[last_char_index].upper()
new_str = str[0:last_char_index]+last_char
print(new_str)
"""

#!2-primer
"""
str = input("Введите строку:")
str=str.lstrip().rstrip()
str_list = str.split(" ")
str_list_len = len(str_list)
print(str_list_len)
"""
#!3-primer
"""
password = input("Введите пароль:")
first_char = password[0]
pass_len = len(password)
if pass_len >= 8 and first_char.upper() == password[0]:
    print("Пароль принят")
else:
    print("Ваш пароль не принят")
"""

