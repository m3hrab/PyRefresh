"""### Exercise 10: **Warehouse Inventory**
You are managing a warehouse inventory system, where items are stored in different locations. Each item has a unique code and multiple locations. Write a program to:
- List all unique item codes.
- Determine which items are stored in multiple locations."""

inventory_data = [
    ('Item001', ['LocationA', 'LocationB']),
    ('Item002', ['LocationA']),
    ('Item003', ['LocationB', 'LocationC']),
    ('Item001', ['LocationC'])
]

unique_code = set([item_code[0] for item_code in inventory_data])
print("Unique codes are:")
print(*unique_code, sep=',')