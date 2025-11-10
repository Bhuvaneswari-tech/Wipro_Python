'''
set - accepet only the unique elements

functions
s = {10,20,30,40,50}
s1 = set([10,20,30,40])

len(s) = Length of the set(number of elements)
min(s) = smallest element
max(s) = Largest element
sum(s) = Total elements
set() = creates a set

Methods

s.add(5) = adds element 5 to the set s
s.remove(30) - removes element 30 from set
s.discard(300) - removes element 300 when its found 
s.pop() - remove an element
s.clear() - Remove all elements
s.union({10,2,3}) = {10,20,30,40,50,2,3} Returns union of two sets
intersection - Return common elements
s.intersection({10,2,3}) - 10
differnce() - Returns elements in first set but not in second set
s.difference({10,20,30}) - 40,50



set is unordered and unique
'''
s = {10,20,30,40,50}
#s.remove(300)
s.discard(300)
s.discard(20)
print(s)