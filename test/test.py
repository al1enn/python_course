
#!1
"""
str = input("enter text:")
str = str.replace(" ", "")
print(len(str))
"""

#!2
"""
arr = ['apple', '3', 'orange', '10']
new_arr = []

for i in arr:
    if i.isalpha():
        new_arr.append(i)
print(new_arr)
"""

#!3
"""
str = input("enter text:")
str = str.replace(" ", "")
arr = []
for i in str:
    arr.append(i)

def count_of_letters(array):
    new_arr = []
    for i in array:
        if array.count(i) > 1 and (i, array.count(i)) not in new_arr:
            new_arr.append((i, array.count(i)))
    return new_arr


result = count_of_letters(arr)
print(result)
"""
#!4
"""
n = int(input("enter number:"))
p = 1
for i in range(1, n+1):
    p *= i
print(p)
"""
#!5
"""
str = input("enter text:")
str = str.rstrip().lstrip().lower()
reverse_str=str[::-1]
if reverse_str==str:
    print("is polindrom")
else:
    print("is not polindrom")
"""
#!6
"""
n = int(input("enter number:"))

def is_fibonaci(number):
    f1 = f2 = 1,1
    arr = [f1, f2]
    counter = 1
    for i in range(2, number+1):
        f1, f2 = f2, f1+f2
        arr.append(f2)
        counter=i
        if f2 == number:
            break
    if number in arr:
        return arr, counter
    return False
print(is_fibonaci(n))
"""
#!7
n = int(input("enter number:"))
arr = []


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True


for i in range(2, n+1):
    if is_prime(i):
        arr.append(i)

print(arr)
