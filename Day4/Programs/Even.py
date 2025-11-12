

# for n in number:
#     if n%2 == 0:
#         print(f"{n} is Even")
#     else:
#         print(f"{n} is Odd")
odd = []
even = []        
def check_even_odd(number):
    for n in number:
        if n%2 == 0:
            even.append(n)
            #print(f"{n} is Even")
        else:
            odd.append(n)
            #print(f"{n} is Odd")
    print("Even numbers: ",even)
    print("Odd number: ", odd)
            
number = [10,23,45,66,78,91,100]
check_even_odd(number)