#Scenario: Online shopping cart system

#initialize the cart

cart = ["Laptop","Mouse","Keyboard","Mouse","Charger"]
print("Initial Cart: ",cart)

#append() - Add a new item to the cart
cart.append('USB Cable')
print('After append: ',cart)

#insert() - Add an item at a specific position
cart.insert(1,"HeadPhones")
print("After insert: ",cart)

#remove() = Remove the first Occurance
cart.remove("Mouse")
print("After remove: ", cart)

#pop() - Remove the last item
popitem = cart.pop()
print(popitem)
print('After pop: ', cart)

#index() - Find the position of an item
position = cart.index("Keyboard")
print("Keyboard is at position: ",position)

cart.append("Mouse")
#count() - how many times an item appears
mouse_count = cart.count("Mouse")
print("Mouse appears:",mouse_count,"times")

original = cart.copy()

#sort() - sort items alphabetically(or numerically)
cart.sort()
print("Sorted cart: ",cart)

#descending order
desc_list = sorted(original,reverse=True)
print("Sorted (Descending): ",desc_list)

#reverse() - Reverse the order of items
cart.reverse()
print("Reversed Cart: ",cart)

#extend() - Add multiple items from another list
wishlist = ["Tablet","Smartphone"]
cart.extend(wishlist)
print("After extending with wishlist: ",cart)

#clear() - Remove all items from the list
cart.clear()
print("After clear: ",cart)