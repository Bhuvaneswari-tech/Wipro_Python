#while loop

#Sum of First N natural number

n = int(input('Enter the number: '))
i=1
total = 0
while i<=n:
    total += i
    i+=1

print('Sum of ',n, ' natural numbers: ',total)