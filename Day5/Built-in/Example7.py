#create a csv file

import csv
# with open("data.csv","w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age"])
#     writer.writerow(["Alice",25])
#     writer.writerow(["John",22])
#     writer.writerow(["Charlie",25])
    
with open("data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)