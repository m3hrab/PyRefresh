"""### Exercise 7: **Popular Tourist Attractions**
You are given a list of tourists visiting various attractions, where each tourist has visited multiple places. Write a program to:
- Count the total number of unique attractions visited.
- Find the top 3 most visited attractions.
"""

tourists_data = [
    ('Tourist1', ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame']),
    ('Tourist2', ['Eiffel Tower', 'Colosseum', 'Louvre Museum']),
    ('Tourist3', ['Eiffel Tower', 'Colosseum', 'Great Wall'])
]

all_visisted_attractions = []
for data in tourists_data:
    all_visisted_attractions.extend(data[1])
    
unique_attractions = list(set(all_visisted_attractions))
print(f"Total number of unique attractions is : {len(unique_attractions)}")
print(*unique_attractions, sep=',')

def custom_sort(place):
    return all_visisted_attractions.count(place)

unique_attractions.sort(key=custom_sort, reverse=True)
print(f"\nTop 3 most visited attractions:")
for i in range(3):
    print(f"{unique_attractions[i]}: {custom_sort(unique_attractions[i])}")