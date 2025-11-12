def factorial(n): # 5 - 5*4*3*2*1
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    #print(f"Factorial of {n} is {fact}")
    return fact

#factorial(5)
n = int(input("Enter the number: "))
print(f"Factorial of {n} is {factorial(n)}")
    

    