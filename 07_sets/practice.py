"""Given the list of visitor IDs below, find how many unique visitors accessed the site."""
visitors = [101, 102, 103, 104, 102, 101, 105, 106, 107, 105]

visitors = set(visitors)
print(f'Unique Visitor: {len(visitors)}')


# Task 2
"""Two users of a social media app have the following interests. Find the common interests between them.
"""
user1_interests = {"python", "data science", "ai", "football", "gaming"}
user2_interests = {"machine learning", "gaming", "python", "music", "ai"}

common_interests = user1_interests.intersection(user2_interests)
print(f"These are the common interests of this two users: {common_interests}")

# Task 3
"""You are given the following list of email addresses with duplicates. Remove the duplicates and return the unique email addresses."""

emails = ["abc@example.com", "xyz@example.com", "abc@example.com", "user@sample.com", "xyz@example.com"]

unique_emails = set(emails)
print(f"Emails: {unique_emails}")

# Task 4
"""You have the following sets of ingredients, one for what you have and one for what the recipe requires. Find which ingredients are missing or extra"""
available_ingredients = {"flour", "sugar", "butter", "eggs", "vanilla", "milk"}
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "baking powder"}

extra_or_missing_ingredients = available_ingredients.symmetric_difference(recipe_ingredients)
print(f"Missing or Extra ingredients: {extra_or_missing_ingredients}")


# Task 5
"""You are given two sets representing employees in the sales and marketing departments. Find out which employees work in both departments."""
sales_department = {"John", "Alice", "Sam", "Tom"}
marketing_department = {"Alice", "Tom", "Emma", "David"}

super_employee = sales_department.intersection(marketing_department)
print(f"{super_employee} works on the both department.")


# Task 6
"""Two people have the following book collections. Find:
a) Books both people have.
b) Books only the first person has.
c) All unique books between both people."""
person1_books = {"The Alchemist", "1984", "The Catcher in the Rye", "Harry Potter"}
person2_books = {"The Catcher in the Rye", "The Great Gatsby", "Harry Potter", "Moby Dick"}

print(f"\na.Books both people have: {person1_books.intersection(person2_books)}")
print(f"b.Books only the first person has {person1_books.difference(person2_books)}")
print(f"c. All unique books between both people: {person1_books.symmetric_difference(person2_books)}")

# Task 7
"""You have two sets: students who attended a class and students who submitted an assignment. Find out which students attended the class but didn't submit the assignment."""
attended_class = {"Alice", "Bob", "Charlie", "David", "Eva"}
submitted_assignment = {"Charlie", "Eva", "Frank", "Alice"}

print("\nTask 7")
bad_students = attended_class.difference(submitted_assignment)
print(f"Bad students: {bad_students}")

# Task 8
"""Given the following list of words extracted from a text file, extract all unique words and count how many there are."""
words = ["python", "code", "python", "data", "machine", "code", "python", "learning"]
unique_words = set(words)

print("Task 8")
print(f"Total unique words: {len(unique_words)}")
print(f"Uniques words are: {unique_words}")

# Task 9 
"""You have two sets: items in your shopping cart and items on your shopping list. Identify any extra items in the cart that are not on your list."""

shopping_cart = {"apples", "bread", "milk", "eggs", "butter", "chocolate"}
shopping_list = {"milk", "bread", "eggs", "apples"}

extra_item = shopping_cart.difference(shopping_list)
print(f"Extra items on the shopping cart: {extra_item}")

# Task 10
"""Given the following list of numbers, find any duplicate numbers using sets.
"""
numbers = [10, 20, 30, 10, 40, 50, 20, 60, 30]
print(set(numbers))
