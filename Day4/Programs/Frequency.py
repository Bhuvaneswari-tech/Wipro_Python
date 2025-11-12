#Find the Frequency of Elements in a List

def element_freq(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item,0)+1
    return freq

data = [1,2,2,3,3,3,4]
print("Element frequency:",element_freq(data))

'''
for item in lst:
item = 1
freq[1] = freq.get(1,0)+1 = 0+1

item = 2
freq[2] = freq.get(2,0)+1 = 0+1 = 1

item=2
freq[2]=freq.get(2,0)+1 = 1+1 = 2

{1:1,2:2}
'''