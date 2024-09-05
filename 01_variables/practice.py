# Variables in python

from typing import Mapping


name = "Mehrab"
age:int = 25 

print(f'Name: {name} \nAge:{age}')
name , age = "Mehrab", 25
print('Name {} \nAge:{}'.format(name,age))


# Data types

# 1. Numeric types
# integer
int_num = 20
# float
float_num = 9.99
# complex
complex_num = 3 + 2j

print(f'Int: {int_num}, Flaot:{float_num}, Complex:{complex_num}')


# 2. String type 
name = "Mehrab"
print(f"String: {name}")

# 3. Boolean type 
flag = True # value either True or False
print(f"Boolean: {flag}")

# 4. Sequence type
# list 
numbers_list = [1,3,4]
# tuple 
tuples = (1,3,4)
# range 
ranges = range(1,10,2)
# string 
name = "Mehrab"

# 5. set type 
numbers = set([2,1,2,3]) # {1,2,3}
print(numbers)
# frozen sets
numbers = frozenset([2,3,1])
print(numbers)

# 6. Mapping types
info = {'name':"Merhab", 'id':22231203043}
print(info)
print(info.keys())
print(info.values())

# Other builtin types
# None types 
flag = None 
n = b"Hello"
print(n)
print(type(n))
n = bytearray([2,3,4])
print(n)
print(type(n))
m = memoryview(b'hello')
print(m)
print(type(m))