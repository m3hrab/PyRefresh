"""### Exercise 4: **Customer Preferences**
You are given two sets of customer preferences for products A and B. Find:
- Customers who prefer only product A.
- Customers who prefer both products.
- Customers who prefer neither."""

product_a_customers = {'Alice', 'Bob', 'Charlie', 'David'}
product_b_customers = {'Charlie', 'David', 'Eve', 'Frank'}

only_product_a_customers = product_a_customers.difference(product_b_customers)
both_products_customers = product_a_customers.intersection(product_b_customers)


all_customers = product_a_customers.union(product_b_customers)
all_customers.add("Mehrab")
customers_who_prefers_neithers = all_customers.difference(product_a_customers.union(product_b_customers))


print(f"Only Product A Prefer:{only_product_a_customers}")
print(f"Prefer Both {both_products_customers}")
print(f"Customers who prefer neither: {customers_who_prefers_neithers}")