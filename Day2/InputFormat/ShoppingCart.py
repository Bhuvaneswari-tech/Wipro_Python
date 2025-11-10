#Shopping Cart Calculator - Menu Driven Program

# d1 = {1:"One",2:"Two"}

# #print Two
# print(d1[2])

print("=============Welcome to Python Store============")

#Fixed Product Prices
products = {
    1:("Notebook",30.0),
    2:("Pen",10.0),
    3:("Bag",75.0)
}

cart_total = 0.0

while True:
    print("\n============Product Menu==========")
    print("1. Notebook - $30.00") 
    print("2. Pen      - $10.00")
    print("3. Bag      - $75.00")
    print("4. Checkout and Exit")
    
    choice = int(input("Select a product (1-4): "))
    
    if choice == 4:
        break
    elif choice in products:
        item_name, price = products[choice] #choice = 1 , products[1]
        qty = int(input(f"Enter quantity of {item_name}: "))
        cost = price * qty
        cart_total += cost
        print(f"Added {qty} X {item_name}(s) = ${cost:.2f}")
    else:
        print("Invalid selection! Please choose from the menu.")

#Apply discount if eligible
if cart_total > 100:
    discount = 0.10 * cart_total
    final_total = cart_total - discount
else:
    discount = 0
    final_total = cart_total
    
print("\n===============Bill Summary==============")
print(f"Cart Total          : ${cart_total: .2f}")
print(f"Discount ( 10% )    : ${discount: .2f}")
print(f"Final Amount        : ${final_total: .2f}")
print("Thank you for shopping with us!")