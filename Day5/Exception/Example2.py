try:
    #f = open("sample.txt","r")
    f = open("Example1.py","r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("this will always execute")
    #print(data)
    f.close()