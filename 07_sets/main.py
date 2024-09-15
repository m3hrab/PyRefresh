# Defination
my_set = {True,3,4, 4, 1, 0, False} # Duplicates are ignored also True and 1 considered as same value, False and 0 is also same 
empty_set = set() # We can't define empty set by {}, as it wold create a dictionary instead.
print(len(my_set))


# Add items
my_set.add("Mehrab")
print(my_set)

my_set2 = ['a', 'A', 'z', False]
my_set.update(my_set2) # change the original sets and doesn't return a new set

my_set.remove(True)
my_set.add(1)
# my_set.remove("asdfa") # raise error if items doesn't exits
my_set.discard("A")
my_set.discard("asdfadsfa")

print(my_set)
print(my_set.pop()) # removes items randomly
print(my_set)
print(my_set.pop())
print(my_set)

# my_set.clear()
# del my_set
print(my_set)


# Join sets

# union() or update() returns a new sets with all the items of both sets
set1 = {1,2,4}
set2 = {'a', 'b', 'c'}

# set3 = set1.union(set2) 
set3 = set1 | set2 # instead of union
print(set3)

# join multiple sets 
set3 = {"Mehrab", "Apple"}
set4 = set1.union(set2, set3)
print(set4)

y = {1,2,3}
z = set1.union(y)
print(z)
# w

# intersection() -> only keeps the duplicates
# new = set1.intersection(y)  -> instead of intersection
new = set1 & y
print(new)

set1.intersection_update(y)
print(set1)



# Difference 
set1 = {"apple", "banana", 'cherry'}
set2 = {"google", "cherry", "mango"}

# set5 = set1.difference(set2) 
set5 = set1 - set2
print(set5)

# difference update change the origianl set instead of reaturn a new set
set1.difference_update(set2)
print(set1)

# Symmetric_difference -> keeps all the items except duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set7 = set1 ^ set2
print(set7, set1)
print(set1)
set1.symmetric_difference_update(set2)
print(set1)