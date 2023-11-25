# value = input("input :")
# print(None if not value else value)

# ! Loop
# word = 'hello'
# new_word=""
# for char in word:
#     if char == 'l':
#         char = 's'

#     new_word += char
# print(new_word)

# counter = 99
# while (counter > 0):
#     if counter % 5 == 0:
#         print(counter)
#     counter -=1

#!Словари
my_dict = {
    "name": 'Timur',
    "age": "25"
}
print("user name:{}\nuser age:{}".format(
    my_dict.get("name"), my_dict.get("age")))
p = my_dict.pop('name')
print(my_dict)
