#Reverse Digits of a Number

'''
n=12345 
digit = n%10 = 12345 % 10 = 5
rev = rev*10 + digit = 0*10 + 5 = 0 + 5 = 5
n = n//10 = 1234

1234>0
digit = 1234%10 = 4
rev = rev*10 + digit = 5*10 + 4 = 50+4 = 54
n = n //10 = 1234 // 10 = 123

123>0
digit = 123%10 = 3
rev = 54*10 + 3 = 540 + 3 = 543
n = 123 // 10 = 12

12>0
digit = 12 % 10 = 2
rev = 543*10 + 2 = 5430 + 2 = 5432
n = 12 // 10 = 1

1>0
digit = 1 % 10 = 1
rev = 5432*10 + 1 = 54320 + 1 = 54321
n= 1 // 10 = 0

0>0
print(rev) = 54321
'''
#056892
#count number of digits
n = int(input('Enter the number: '))
rev = count = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    count+=1
    n = n //10

print('Reverse the digit: ',rev)
print('Number of digits: ', count)
    
