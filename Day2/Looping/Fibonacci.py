'''
Fibonacci Series

0 1 1 2 3 5 8 13

num = 5

a=0, b=1
0 1 1 2 3 

next value = add(current value+prev value)
'''

n = int(input('Enter the number of series: ')) #n= 5
prev= 0
current=1 #from current value changed into prev value
print(prev,end=' ')
print(current,end=' ')
count = 2
while count<n:
    result = current+prev #1+1 = 2 
    print(result,end=' ')
    prev = current #prev= 1
    current = result #current = 1, 2
    count +=1
    
    
