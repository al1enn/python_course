# value = input("input :")
# print(None if not value else value)

# ! Loop
"""
word = 'hello'
new_word=""
for char in word:
    if char == 'l':
        char = 's'

    new_word += char
print(new_word)
"""
"""
counter = 99
while (counter > 0):
    if counter % 5 == 0:
        print(counter)
    counter -=1
"""
#!Словари
"""
my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]
count_dict = {
}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
for key, value in count_dict.items():
    print("Key:", key, "count", value)
"""
"""
my_dict = {"alice": 35, "mark": 25, "april": 45, "john": 20}
new_d = {}
for key, value in my_dict.items():
    if key[0] != 'a':
        new_d[key] = value
print(new_d)
"""

#!Функции

"""
def max_value(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max if max > 0 else "max value is less then zero"


a = [-45, -34, -4, 0]
result = max_value(a)
print(result)
"""
"""
def power(value, value_power):
    if value_power >=0:
        return value**value_power

a = int(input("Enter value:"))
b = int(input("Enter value for power:"))
result = power(a, b)
print(result)
"""
#!Функции 2-часть

