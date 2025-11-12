#Built in modules are already included in the python
import math

#calculate circle area and Hypotenuse

r = 5
area = math.pi * r **2
print("Area of a circle:",round(area,2))
print("Hypotenuse(3,4):",math.hypot(3,4))

#Calculate Factorial
n = 5
print(f"factorial of {n} is {math.factorial(n)}")

#Square root and power
x = 16
print(f"Square root of {x} is {math.sqrt(x)}")
print(f"2 raised to power 3 is {math.pow(2,3)}")

#Rounding numbers
n = 7.8
print("Ceiling:",math.ceil(n))
print("Floor:",math.floor(n))

#Trigonometry
angle = math.pi/2
print("sin(pi/2) =",math.sin(angle))
print("cos(pi/2) =",math.cos(angle))

#Greatest Common Divisor - GCD
a,b=30,60
print(f"GCD of {a} and {b} is {math.gcd(a,b)}")