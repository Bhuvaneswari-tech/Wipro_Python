'''
      1
     2 3
    4 5 6
   7 8 9 10
11 12 13 14 15 
'''

n = int(input('Enter the number of rows: '))
#space = n

# while i<=n:
#     space = i
#     while space<=n:
#         print('',end=' ')
#         space+=1
#     while i>=1
num = 1
for i in range(1,n+1):
    for space in range(i,n):
        print('',end=' ')
    for j in range(1,i+1):
        print(num,end=' ')
        num+=1
    print()
    
#Amstrong number = 153, 9474
'''
sum(153) = 1 cube + 5 cube + 3 cube

if original number == sum
print Amstrong number

sum(9474) = 9 power 4 + 4 power 4 + 7 power 4 + 4 power 4


'''