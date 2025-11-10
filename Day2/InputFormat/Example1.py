#Employee details
'''
empid = int(input('Enter the Employee id: '))
name = input('Enter the Employee name: ')
salary = float(input('Enter the salary: '))
jobrole = input('Enter the Role: ')
'''
#Take one character as input
# char = input('Enter a single character: ')[0]
# print('Character value: ',char)

#Take multiple inputs in one line
#12 13 , x = 12 y=13
# x,y = input('Enter two numbers seperated by space: ').split()
# print('x and y value: ',x,y)

# #User input to Boolean
# is_member = input('Are you a member(yes/no): ').lower() == 'yes'
# print('member value is: ',is_member)

# #l1 = [1,2,3,4,5]
# #1 2 3 4 5
# l1 = list(map(int,input("Enter list of numbers: ").split()))[:5]
# print('List1: ',l1)

# #1,2,3,4,5 - Getting input from user with comma seperated
# l2 = list(map(int,input("Enter list of numbers: ").split(',')))
# print('List2: ',l2)

#Remove the leading/trailing spaces from the input
sentence = input('Enter a sentence: ').strip()
print(sentence)