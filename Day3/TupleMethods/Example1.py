#PRoduct Management system
'''
Scenario:
A small company stores the number of products sold each day in a tuple.
sales = (15,20,15,30,20,20,25)

Tasks:
1. Find the total number of products sold in a week
2. Identity the day(s) when the maximum sales done
3. Count how many days had sales equal to 20
'''

sales = (15,20,15,30,20,20,25)

#Total Sales
total_sales = sum(sales)
print("Total Sales: ", total_sales)

#Maximum sales
max_sales = max(sales)
max_index = sales.index(max_sales)
print('Maximum sales: ',max_sales, "on day",max_index+1)

#count of days with sales = 20
day_20_sales = sales.count(20)
print("Number of days with sales = 20:",day_20_sales)

#reverse
# sales.reverse()
# print('REverse the tuple: ',sales)

'''
Function 
len(), min(), max(), sum(), sorted()

Methods:
count(obj), index(obj)
'''