# Product 1 and Product 2 tags
product_1_tags = {"Electronics", "Laptop", "Gaming", "NewArrival"}
product_2_tags = {"Laptop", "Office", "Electronics", "Discount"}

# 1. Add a new tag "Portable" to Product 1
product_1_tags.add("Portable")
print("Product 1 tags after adding 'Portable':", product_1_tags)

# 2. Remove the tag "NewArrival" from Product 1
product_1_tags.remove("NewArrival")
print("Product 1 tags after removing 'NewArrival':", product_1_tags)

# 3. Check if "Gaming" is a tag for Product 1
is_gaming_tag = "Gaming" in product_1_tags
print("Is 'Gaming' a tag for Product 1?", is_gaming_tag)

# 4. Find all unique tags across Product 1 and Product 2 (Union)
all_tags = product_1_tags.union(product_2_tags)
print("All unique tags across both products:", all_tags)

# 5. Find tags common to both products (Intersection)
common_tags = product_1_tags.intersection(product_2_tags)
print("Tags common to both products:", common_tags)
