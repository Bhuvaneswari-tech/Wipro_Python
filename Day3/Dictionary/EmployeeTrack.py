'''
Scenario:
A company tracks employees and their current project
'''

#Employee dictionary
employees = {
    "E101": "Website Revamp",
    "E102": "Mobile App",
    "E103": "Data Analysis"
}

#Get the project of an employee
print("E102 is working on: ",employees["E102"])
print("E102 is working on: ",employees.get("E102"))

#Add a new employee
employees["104"]="Cloud Migration"

#Remove an employee
employees.pop("E103")

print(employees.keys())
print(employees.values())

#List all employees and their projects
for emp_id, project in employees.items():
    print(emp_id, "=>" , project)

#Update project of an employee
employees.update({"E101":"Website Redesign"})

print("Updated Employees Dictionary:",employees)
