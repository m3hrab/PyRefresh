# Define a list 
numbers = [1, 3, 5]

# Accessing element from a list 
print(f'{numbers[1]} is the second elements of {numbers} list')

# Modifying element from a list 
numbers[1] = 20

# Adding elements
# ADD element end of the list using append() method 
numbers.append(33)

# Add element at first index 
numbers.insert(0, 20)

# Adding multiple items at once
numbers.extend([121,121,12])


# Removing element 
# Remove by value 
numbers.remove(20)

# Remove by index 
numbers.pop(-2)

# Remove multiple items at once
del numbers[1:len(numbers)-1]

# Delete the entire list
numbers.clear()
print(numbers)

# List comprehension
numbers = [10, 1, 20, 2, 5, 22]

even_numbers = [number for number in numbers if number %2 ==0 ]
test = ["even" if x%2==0 else "odd" for x in numbers]
print(even_numbers)
print(test)

# list sort 
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Customize the sort function
def closerTo10(number):
    return abs(number - 10)

numbers.sort(key=closerTo10)
print(numbers)

# Case insensitive sort
n = ['banana', "Apple", 'mango', 'Orange', 'Coconuts']
n.sort(key=str.lower) 
print(n)

# Different types copy of list

fruits = n.copy()
favorite_fruits = list(fruits)
most_favorite_fruits = favorite_fruits[:]

# Join a list
dummy = numbers + fruits
dummy.extend(n)
print(dummy)