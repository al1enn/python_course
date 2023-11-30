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

"""
x = [1, 2, 3, 4, 5]

def make_smth(function):
    for el in x:
        print(function(el))
        
make_smth(lambda a: a+10)
"""

# ? Рекурсия
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
"""

#! Исключения
"""
try:
    c = 10/0
except:
    c = 0
    print('An exception occurred')

print(c)
"""

"""
def x():
    a = 10


x = True
try:
    # print(a)
    # print(int('abc'))
    for el in x:
        print(x)
except ValueError as error:
    print(error)
except NameError as error:
    print(error)
except TypeError as error:
    print(error)
"""

"""
def get_month(number):
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    try:
        return months[number]
    except KeyError as error:
        print(error, ", use only numbers from 1 to 12")
    except TypeError as error:
        print(error, ", use only numbers from 1 to 12")


month_name = get_month([1, 2, 3])
print(month_name)
"""

"""
def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as error:
        print(error, "use only strings,lists or sets")


s = 'abcdd'
u = check_sequence_unique(s)
print(u)
"""
