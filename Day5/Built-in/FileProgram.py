#f = open("demofile.txt","r")
#print(f.read())

#return one line
#print(f.readline())

# for x in f:
#     print(x)

# f1 = open("demofile.txt","a")
# f1.write("\nNow the file has more line!")
# f1.close()

# f1 = open("demofile.txt","r")
# print(f1.read())
# f1.close()

f1 = open("demofile.txt","w")
f1.write("Oops! I have deleted the content!")
f1.close()