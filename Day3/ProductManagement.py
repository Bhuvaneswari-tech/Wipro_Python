#E-Commerce Product Management System using list, tuple, dictionary, and set methods/functions
# Initial list of products
products = [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 70000, "tags": {"Electronics", "Portable"}, "ratings": (5, 4, 5)},
    {"id": 102, "name": "Smartphone", "category": "Electronics", "price": 40000, "tags": {"Electronics", "Mobile", "Portable"}, "ratings": (4, 5, 4, 5)},
    {"id": 103, "name": "Office Chair", "category": "Furniture", "price": 8000, "tags": {"Furniture", "Office"}, "ratings": (4, 4, 3)},
]

# 1. Add a new product
new_product = {"id": 104, "name": "Headphones", "category": "Electronics", "price": 3500, "tags": {"Electronics", "Audio"}, "ratings": (5, 4)}
products.append(new_product)

# 2. Update price of product 102
for product in products:
    if product["id"] == 102:
        product["price"] = 42000
        print(f"Product {product['id']} ({product['name']}) new price: {product['price']}")

# 3. Add a new tag "Discount" to product 101
for product in products:
    if product["id"] == 101:
        product["tags"].add("Discount")
        print(f"Product {product['id']} tags: {product['tags']}")

# 4. Calculate average rating for each product
print("\nAverage ratings per product:")
for product in products:
    ratings = product["ratings"]
    average = round(sum(ratings)/len(ratings), 2) #product the output with 2 decimal
    print(f"{product['name']}: {average}")

# 5. List all unique tags across all products
all_tags = set()
for product in products:
    all_tags.update(product["tags"])
print("\nAll unique tags across products:", all_tags)

# 6. List all unique product categories
all_categories = set()
for product in products:
    all_categories.add(product["category"])
print("All unique product categories:", all_categories)
