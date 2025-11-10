#Pattern Program

'''
1
12
123
1234
12345

number of rows=5
i=1
while i<=n => 2<=5

j = 1

while j<=i => 1<=1 , j=2 2<=2

print j = 1 2
j+=1 => j=3

i+=1 => i=2

2<=5
print j = 1
'''

n = int(input('Enter the number of rows: '))
i = 1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    print()
    i+=1
    
'''
1
22
333
4444
55555
'''