# List
# Define a list 
users = ["m3hrab", "to0th_less", "youKn0wWho","misorin", "tourist"]

# Accessing element from a list 
first_user = users[0]
last_user = users[-1]

print(f"First user:{first_user}\nLast User:{last_user}")

# Modify list 
# changing the second users name
users[1] = 'LightFury'
print(users)

# change a range of items values 
users[2:4] = ['testuser1', 'testuser2']


# Slicing
kings_of_cp = users[1:5]
print(f"Kings of Codeforces: {kings_of_cp}")
warrior_of_cp = users[:1]
print(f"Warrior of Codeforces: {warrior_of_cp}")

# Adding elements 
users.append('to0th_less')
print(users)

# Adding element at a specific postion
users.insert(2, 'bruteforceman')
print(users)

# Extend the list
users.extend([1,3,4])
# Removing element from a list
users.remove('testuser1')  # Remove by value
print(users)
users.pop(3) # Remove by index
print(users)

# delete the specific items using index or range
del users[-3:]
print(users)
# clear the list
users.clear()
print(users)