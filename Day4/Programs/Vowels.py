#Education

def count_vowels(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            count+=1
    print(f"Count of Vowels for {s} is {count}")
    
str = "Education"
count_vowels(str)

'''
Find the Frequency of Elements in a List

'''