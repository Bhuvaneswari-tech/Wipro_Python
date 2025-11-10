#Check if a Number is Palindrome

'''
n = 121
rev = 121

n == rev
n is called palindrome

n = 123
rev = 321

n == rev = not true
n is not a palindrome
'''

n = int(input('Enter the number: '))
temp = n
rev = 0
while n>0:
    digit = n%10
    rev = rev *10 + digit
    n = n // 10
    
if(temp == rev):
    print(temp ,'is a palindrome')
else:
    print(temp,' is not a palindrome')
    
#input n  121 , 12325, 12121