import numbers

#check number type
a = 10
print(type(a))

print(isinstance(10,numbers.Integral))

age = 23
if isinstance(age,numbers.Integral):
    if age>=18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("Invalid input")

print(isinstance(10.5,numbers.Real))
print(isinstance(3+5j,numbers.Complex))