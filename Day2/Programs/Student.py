# 1. Data Setup
Raw_Student_Data = [
    'John: Math, 92: pass',
    'Alice: Science, 78: fail',
    'Bob: Math, 89: pass'
]

# 2. Structuring Data
Structured_Student_List = []

for record in Raw_Student_Data:
    parts = record.replace(',', ':').split(':')
    #print(parts)
    Name = parts[0].strip()
    Subject = parts[1].strip()
    Marks = int(parts[2].strip())
    Status = parts[3].strip()
    Structured_Student_List.append((Name, Subject, Marks, Status))
print(Structured_Student_List)

# 3. Analysis and Reporting
High_Scorers = set()
for student in Structured_Student_List:
    if student[2] >= 85:
        High_Scorers.add(student)

# Print last two records using slicing
print("Last two student records:", Structured_Student_List[-2:])

# Generate formatted report
first_student = Structured_Student_List[0]
report = f"STUDENT REPORT: {first_student[0].upper()} scored {first_student[2]} in {first_student[1]}"
print(report)

# Summary
print("High Scorers Set:", High_Scorers)