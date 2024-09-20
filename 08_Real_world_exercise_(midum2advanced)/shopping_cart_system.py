"""### Exercise 3: **Shopping Cart System**
You are building a shopping cart system for an e-commerce website. Write a function that:
- Accepts a list of item names and their prices.
- Outputs the total cost, and ensures no item appears more than once.

"""
cart_items = [
    ('Laptop', 999.99),
    ('Mouse', 19.99),
    ('Keyboard', 49.99),
    ('Laptop', 999.99)
]

def calculate_total_cost(cart_items):
    """Outputs the total cost, and ensures no item appears more than once."""
    calculated_items = set()
    total_cost = 0
    for cart_item in cart_items:
        if cart_item not in calculated_items:
            total_cost += cart_item[1]
            calculated_items.add(cart_item)
    
    return total_cost


print(f"Print total cost: {calculate_total_cost(cart_items)}")