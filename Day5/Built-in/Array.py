import array

arr = array.array('i',[1,2,3,4,5])
print(arr)

# l1 = [1,2.5,3,4,5]
# print('L1=',l1)
#i represents an integer type

#Append element
arr.append(40)
print(arr)

#Access by index
print(arr[2])

#insert and remove
arr.insert(1,15)
arr.remove(40)
print(arr)

#convert to list
print(arr.tolist())