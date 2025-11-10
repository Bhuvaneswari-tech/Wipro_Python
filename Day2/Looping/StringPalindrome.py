str = input('Enter the string: ')
rev = str[::-1]

#Malayalam = malayalaM

if str.lower() == rev.lower():
    print('Palindrome')
else:
    print('Not a palindrome')
    
'''
Fibonacci Series

0 1 1 2 3 5 8 13

num = 5

a=0, b=1
0 1 1 2 3 

next value = add(current value+prev value)
'''