#List is mutable - you can update the value
x = [10,12.55,'Hi',True]
print(x) #[10,12.55,'Hi',True]
print(x[0]) #10
print(x[1:]) #12.55,'Hi',True
x[1] = 200
print(x) #[10, 200, 'Hi', True]
print(x[::-1]) #Reverse order
print(*x) #without square bracket
tinylist = [123,'john']
print(x + tinylist) #print concetenated lists