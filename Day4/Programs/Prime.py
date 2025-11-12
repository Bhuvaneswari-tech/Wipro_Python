# n = 5

# 5/5 
# 5/1
# 2,3,4

# n=6
# 6/6
# 6/1
# 2,3,4,5
# for i in range(2,n)

# 6/2 = 3 = n%i
# 2,3
# for i in range(2,n/2+1)

n = int(input("Enter the number: "))

if n>1:
    for i in range(2,n//2+1):
        if n%i == 0:
            print(n," is not a prime number")
            break
    else:
        print(n," is a prime number")    
else:
    print(n," is not a prime number")