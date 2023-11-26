
#!Begin
import math
# ? 19
"""
x1 = int(input("Введите x1:"))
y1 = int(input("Введите y1:"))
x2 = int(input("Введите x2:"))
y2 = int(input("Введите y2:"))
a = y2
b = abs(x2-x1)
p = 2*(a+b)
s = a*b
if y2 == y1 and (x1 != 0 or x2 != 0) and x2 < 0:
    print("Площадь={} Периметр={}".format(s, p))
else:
    print("Введите правильные координаты прямоугольника")
"""

# ? 21
"""
x1 = int(input("Введите x1:"))
y1 = int(input("Введите y1:"))
x2 = int(input("Введите x2:"))
y2 = int(input("Введите y2:"))
x3 = int(input("Введите x3:"))
y3 = int(input("Введите y3:"))
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x3-x1)**2 + (y3-y1)**2)
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
if a < b+c and b < a+c and c < a+b:
    print("Площадь={} Периметр={}".format(s, p))
else:
    print("Введите правильные координаты треугольника")
"""
# ? 22
"""
a = int(input("Введите A:"))  # 4
b = int(input("Введите B:"))  # 5

d = a
a = b
b = d
#! ez way 
# a, b = b, a
print("a={} b={} ".format(a, b))
"""

# ? 23
"""
a = int(input("Введите A:"))  # 4
b = int(input("Введите B:"))  # 5
c = int(input("Введите C:"))  # 6

d = c  # d=6
c = b  # b=>c=>c=5
b = a  # a=>b=>b=4
a = d  # c=>a=>a=6

#! ez way a,b,c=c,a,b
print("a={} b={} c={}".format(a, b, c))
"""

# ? 24
"""
a = int(input("Введите A:"))  # 4
b = int(input("Введите B:"))  # 5
c = int(input("Введите C:"))  # 6

d = a  # d=4
a = b  # b=>a=>a=5
b = c  # c=>b=>b=6
c = d  # a=>c=>c=4
#! ez way a,b,c=b,c,a
print("a={} b={} c={}".format(a, b, c))
"""
