import re

txt = "The rain in Spain"
x = re.search("^the.*Spain$",txt)
if(x):
    print("Yes! we have a match!")
else:
    print("No match!")