# Initial marks of Class A
marks = [85, 90, 78, 92, 88, 76, 95, 89]
print("Initial Marks:", marks)

# -------------------------------
# New Admission
# -------------------------------
new_student_mark = 82
marks.append(new_student_mark)
print("\nAfter New Admission (82 added):", marks)

# -------------------------------
# Merging Data from Class B
# -------------------------------
class_b_marks = [80, 91, 87]
marks.extend(class_b_marks)
print("\nAfter Merging Class B:", marks)

# -------------------------------
# Transfer Case
# -------------------------------
marks.remove(76)  # student who scored 76 transfers out
print("\nAfter Transfer (76 removed):", marks)

# -------------------------------
# Error Correction
# -------------------------------
# Suppose last entry was a duplicate or wrongly entered
marks.pop()
print("\nAfter Error Correction (last entry removed):", marks)

# -------------------------------
# Performance Review
# -------------------------------
highest = max(marks)
lowest = min(marks)
total = sum(marks)
count_students = len(marks)
average = total / count_students

# Find position of a specific score, e.g., 89
position_89 = marks.index(89)  # zero-based index

# Count how many students scored 90
count_90 = marks.count(90)

print("\n--- Performance Review ---")
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Total Marks:", total)
print("Number of Students:", count_students)
print("Average Marks:", round(average, 2))
print("Position of 89:", position_89)
print("Number of students who scored 90:", count_90)

# -------------------------------
# Optional: Display all marks sorted
# -------------------------------
marks.sort(reverse=True)
print("\nMarks Sorted Descending (Top to Bottom):", marks)
