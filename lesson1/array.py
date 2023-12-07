import random as r
my_list = []
for i in range(0, 100):
    my_list.append(r.randint(1, 10))
print(my_list.count(2))
