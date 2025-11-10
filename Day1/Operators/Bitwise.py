# &, | , ^ , ~ , << , >>

a = 5 # binary 0101
b = 3 # binary 0011

print('a & b = ',(a&b)) # 0001
print('a | b = ',(a|b)) # 0111
print('a ^ b = ',(a^b)) # 0110
print("~a =", ~a) 
# bitwise NOT -> -6 (two's complement)
print("a << 1 =", a << 1) # 0101 << 1 = 1010 -> 10
print("a >> 1 =", a >> 1) # 0101 >> 1 = 0010 -> 2
