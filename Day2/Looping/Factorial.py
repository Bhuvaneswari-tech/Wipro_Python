#Factorial of a given number

'''
n = 5
fact = 1*2*3*4*5 = 120

fact = 1

while n>0
fact = fact * n = 1*5 = 5
n = n-1 = 4

4>0
fact = 5*4 = 20
n = 4-1 = 3

3>0
fact = 20 * 3 = 60
n = 3-1 =2

2>0
fact = 60 * 2 = 120
n=2-1 = 1

1>0
fact = 120 * 1
n=1-1 = 0

0>0

'''

n = int(input('Enter the number: '))
fact = 1
while n>0:
    fact = fact * n
    n = n-1

print('Factorial of a given number: ', fact)