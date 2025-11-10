# 1. Data Setup
Raw_Employee_Data = [
    'E101: Dev, completed 5 tasks: active',
    'E102: QA, completed 2 tasks: pending',
    'E103: Dev, completed 8 tasks: active'
]

# 2. Structuring Data
Structured_Employee_List = []

for entry in Raw_Employee_Data:
    parts = entry.replace(',', ':').split(':')
    EmpID = parts[0].strip()
    Role = parts[1].strip()
    Tasks = parts[2].replace('completed', '').replace('tasks', '').strip()
    Status = parts[3].strip()
    Structured_Employee_List.append((EmpID, Role, int(Tasks), Status))

# 3. Analysis and Reporting
Pending_Employees = set()
for emp in Structured_Employee_List:
    if 'pending' in emp[3].lower():
        Pending_Employees.add(emp)

# Print first two employees using slicing
print("First two employee records:", Structured_Employee_List[:2])

# Generate formatted report for last employee
last_emp = Structured_Employee_List[-1]
report = f"EMPLOYEE SUMMARY: {last_emp[0].upper()} from {last_emp[1]} team completed {last_emp[2]} tasks."
print(report)

# Summary Output
print("Pending Employees Set:", Pending_Employees)