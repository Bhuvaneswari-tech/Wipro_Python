Base_Units = 250
Rate_Per_Unit = 5.75
Service_Flags = 9

Total_Cost = Base_Units * Rate_Per_Unit
if Base_Units > 300:
    Total_Cost *= 1.10

Final_Bill_Int = int(Total_Cost)
is_High_Usage = Base_Units > 300
if is_High_Usage:
    Service_Alert = (Service_Flags & 1) != 0 # T & T = 1 != 0 = True
else:
    Service_Alert = (Service_Flags & 0) != 0 # T & F = 0 !=0 = False
    
print("Total_Cost:", Total_Cost)
print('Final Bill Int: ',Final_Bill_Int)
print('is High Usage: ',is_High_Usage)
print('Service Alert: ',Service_Alert)