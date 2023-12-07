import random
#!Array

# ? 2
"""
n = int(input("Введите целое число N>0:"))
a = []
for i in range(1, n+1):
    a.append(2**i)

print(a)
"""
# ? 3
"""
n = int(input("Введите целое число N>1:"))
a = int(input("Введите первый член A арифметической прогрессии:"))
d = int(input("Введите разность D арифметической прогрессии:"))
my_list = []
for i in range(0, n):
    my_list.append(a+i*d)
print(my_list)
"""

# ? 4
"""
n = int(input("Введите целое число N>1:"))
a = int(input("Введите первый член A арифметической прогрессии:"))
d = int(input("Введите разность D арифметической прогрессии:"))
my_list = []
for i in range(0, n):
    my_list.append(a*(d**i))
print(my_list)
"""
# ? 5
"""
n = int(input("Введите целое число N>2:"))
f1 = f2 = 1
f3 = 0
my_list = [f1, f2]
for i in range(2, n):
    # f1, f2 = f2, f1+f2 
    # my_list.append(f2)
    f3 = f1+f2
    f1 = f2
    f2 = f3
    my_list.append(f3)
print(my_list)
"""
# ? 6
"""
n = int(input("Введите целое число N>2:"))
a = int(input("Введите целое число A:"))
b = int(input("Введите целое число B:"))
my_list = [a, b]
next_el = 0
for i in range(2, n):
    next_el = sum(my_list)
    a = b
    b = next_el
    my_list.append(next_el)
print(my_list)
"""
# ? 7
"""
n = int(input("Введите размер массива: "))
arr = []
arr_reverse = []
# arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
for i in range(0, n):
    arr.append(random.randint(1, 100))
print("Массив:", arr)

# * 1-way
# for i in range(1,len(arr)+1):
#     arr_reverse.append(arr[len(arr)-i])
# print(arr_reverse)
# * 2-way
# arr_reverse = arr[::-1]
# print(arr_reverse)
# * 3-way
# for element in reversed(arr):
#     arr_reverse.append(element)
# print(arr_reverse)
# * 4-way
# arr_reverse = list(reversed(arr))
# print(arr_reverse)
# * 5-way
arr.reverse()
print(arr)
"""

# ? 8
"""
n = int(input("Введите размер массива: "))
arr = []
k = 0
for i in range(0, n):
    arr.append(random.randint(1, 100))
print("Массив:", arr)

for el in arr:
    if el % 2 == 1:
        print("Элемент:", el, "Индекс:", arr.index(el))
        k += 1
print("Количество нечетных чисел: "+str(k))
"""
n = int(input("Введите размер массива: "))
arr = []
k = 0
for i in range(0, n):
    arr.append(random.randint(1, 100))
print("Массив:", arr)

for el in reversed(arr):
    if el % 2 == 0:
        print("Элемент:", el, "Индекс:", arr.index(el))
        k += 1
print("Количество четных чисел: "+str(k))
