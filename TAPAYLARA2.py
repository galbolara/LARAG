def selection_sort_products(products, key):
    n = len(products)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if products[j][key] < products[min_index][key]:
                min_index = j
        products[i], products[min_index] = products[min_index], products[i]
    return products

inventory = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300},
    {"name": "USB Cable", "price": 10}
]

sorted_inventory = selection_sort_products(inventory, "price")

print("Inventory sorted by price:")
for item in sorted_inventory:
    print(f"- {item['name']}: ${item['price']}")