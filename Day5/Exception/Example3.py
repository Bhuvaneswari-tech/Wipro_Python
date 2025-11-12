#Raising an Exception
age = int(input("Enter your age:"))

if age<18:
    raise ValueError("Age must be at least 18!")
else:
    print("You are eligible to vote")