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