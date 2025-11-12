#datetime module

import datetime

#current date and time
date1 = datetime.datetime.now()
print("Current date and time:",date1)

#Extracting date components
today = datetime.date.today()
print("Year:",today.year,"Month:",today.month,"Day:",today.day)

#Creating a custom date
my_bday = datetime.date(1995,10,22)
print("My birthday:",my_bday)

#Formating dates
print("Formatted date:",date1.strftime("%A, %d %B %Y %I:%M %p"))

print("24 hour time:",date1.strftime("%H:%M"))
'''
%A - Full weekday name = monday
%d - Day of the month - 01, 15, 30
%B - Full month name
%Y - 4 digit year
%I - Hour
%M - minutes
%p - AM/PM
'''