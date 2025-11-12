#Basic try-except

try:
    x = int(input("Enter a number:"))
    print(10/x)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter a valid number")