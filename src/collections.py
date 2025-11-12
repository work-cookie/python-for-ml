# Collections
"""
1. list - [] - ordered items
2. dictionary - {} - key, value 
3. Tuple - () - fixed constants, like cordinates
4. Set - distinct items
"""

x = 100
my_list = [10, "Sachin", True, x]
print(len(my_list))
print(my_list[0:])
print(my_list[-1:]) # last element only in list

my_list.append("Ganguly")
print(my_list)

my_list.insert(1, "Dravid")
print(my_list)

my_list.remove(10)
print(my_list)

print(my_list.pop()) # remove and pop last element
print(my_list)


# 2. Dictionary
person = {
    "name" : "Sachin",
    "age" : 25,
    "profession" : "Cricketer"
}
print(person)
print(person.keys()) # dict_keys
for i in person.keys():
    print(i)

for i in person.items():
    print(i)

print("age" in person) # True
person.update({"color": "green"})
print(person)


# 3. Tuple - Immutable sequences, fixed constants
x = (10,20)
print(x)
print(x[0])
x[0] = 100 # error - TypeError: 'tuple' object does not support item assignment


# 4. Set - bag of same and distinct items
numbers = set() # create an empty set
values = {10, 20, 10, 10, 30}
print(values) # {10, 20, 30}

values.add(100)
values.remove(10)
values.remove(200) # KeyError: 200 - if key not found
values.discard(200)
print(values)

values.add(2000)
print(values)
