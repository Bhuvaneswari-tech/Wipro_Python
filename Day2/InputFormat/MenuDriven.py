#Menu driven Calculator using match-case

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))


print("\n============== MENU ================\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input('Enter your choice (1-4): '))

match choice:
    case 1:
        print("Result: ",num1+num2)
    case 2:
        print("Result: ",num1-num2)
    case 3:
        print("Result: ",num1*num2)
    case 4:
        if num2!=0:
            print("Result: ", num1/num2)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid Choice!")