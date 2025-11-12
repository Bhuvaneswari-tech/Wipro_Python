#Display the month calendar

import calendar
#print(calendar.month(2025,11))

#Check whether the year is leap year or not
print(calendar.isleap(2024))

#count leap years in a range
print(calendar.leapdays(2000,2025))

#display all leap years between the range
start = 2000
end = 2025
for year in range(start,end+1):
    if (calendar.isleap(year)):
        print(year,end=' ')
print()

print(calendar.weekday(2025,11,12))
day_index = calendar.weekday(2025,11,12)
print(calendar.day_name[day_index])

#year is divisible by 4 and not divisible by 100
#year is divisible by 400

# def is_leap(year):
#     if(year%4 == 0 and year%100 !=0) or (year%400 == 0):
#         return True
#     else:
#         return False

# year = int(input('Enter a year: '))
# if is_leap(year):
#     print(f"{year} is a Leap Year!")
# else:
#     print(f"{year} is not a Leap Year!")