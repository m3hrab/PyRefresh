# Definition
# cordinates = tuple([1,3,4])
cordinates = (10, 2)
# print(type(cordinates))
print(cordinates)

# Accessing items
dimensions = (1920, 1080)
width = dimensions[0]
height = dimensions[-1] # negative index 

print(width, height)

months = ("January", "February", "March", "April")
print(months[1:3]) # Slicing -> returns a new tuple

# del months
# print(months)

# Unpacking tuples
first, second, *rest = months
first, *middle, last = months
print(first, middle, last)

# Join tuples 
new = cordinates + months
print(new)

# multiply tuples
new2 = cordinates * 2
print(new2)