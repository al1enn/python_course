
#!1-Kiritilgen soz hammesi ulken harip ekenligin tekserin
"""
str = input("Введите слово:")
str = str.lstrip().rstrip().replace(' ', '')
counter = 0
for char in str:
    if char.isupper():
        counter += 1
if counter == len(str):
    print("hammesi ulken harip")
else:
    print("kishi harip bar")
"""

# ! 2-Kiritilgen soz bas harip penen baslansa hammesin bas harip kishi bolsa hammesin kishi harip penen kiritin.
"""
str = input("Введите слово:")
str = str.lstrip().rstrip()
first_char = str[0]
if first_char.isupper() and first_char.isalpha():
    print(str.upper())
elif first_char.islower() and first_char.isalpha():
    print(str.lower())
else:
    print("Первый символ должен быть буквой")
"""

#! 3-Kiritilgen soz palindrom bolsa True qaytarsin, bolmasa False. (Palindrom – internetten izlen! Misali aziza)
# ? 1-way
"""
str = input("Введите слово:")
str = str.lstrip().rstrip()
str_reverse = str.lower()[::-1]
print(str_reverse)
if str_reverse == str.lower():
    print(f"Слово '{str}' является полиндромом")
else:
    print(f"Слово '{str}' не является полиндромом")
"""
# ? 2-way
"""
str = input("Введите слово:")
str = str.lstrip().rstrip()
reverse_str = ""
index = len(str)-1
while index >= 0:
    reverse_str += str[index]
    index -= 1
if reverse_str == str:
    print(f"Слово '{str}' является полиндромом")
else:
    print(f"Слово '{str}' не является полиндромом")
"""

#!4-Kiritilgen gap neshe soz ham neshe haripten turatuginligin aniqlawshi programma duzin.

str = input("Ввод:")
str = str.lstrip().rstrip()
str_list = str.split(" ")
str_space_removed = str.lstrip().rstrip().replace(' ', '')
str_letters = len(str_space_removed)
str_words = len(str_list)

print("Words: {}\nLetters: {}".format({str_words}, {str_letters}))
