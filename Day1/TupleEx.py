#Tuple is immutable - you cannot update the value
tup1 = (10,20,'Hi',12.45)
print(tup1)
print(tup1[1:])
print(tup1[::-1])
#tup1[1] = 100
#print(tup1)
print(*tup1)
