# --------------------------------------------
# Challenge 2: Library Book Tracking and Late Fee Management
# --------------------------------------------

# 1. Data Structures Setup
Issued_Books = {
    'M-102': ['Python Basics', 'AI Fundamentals'],
    'M-205': ['Data Science', 'OS Concepts', 'Python Basics'],
    'M-310': ['DBMS Principles', 'Computer Networks', 'AI Fundamentals']
}

Reference_Books = {'Python Basics', 'DBMS Principles'}

# 2. Filtering and Analysis (Loop/in/Update)
Late_Fee_Members = []   # List to store members who might have late fees

for member_id, books in Issued_Books.items():
    # Membership check for required reference book
    if 'Python Basics' not in books:
        print("{} missed required reference book.".format(member_id))
    
    # Condition: 3 or more books = possible late fee
    if len(books) >= 3:
        Late_Fee_Members.append(member_id)

# 3. String Processing and Formatting
Member_Tuple = tuple(Issued_Books.keys())              # Convert keys to tuple
Audit_Code = '#'.join(Member_Tuple)                    # Join with #
Sliced_Code = Audit_Code[2:9]                          # Slice from index 2 to 9
Final_Code = Sliced_Code.upper()                       # Convert to uppercase

# 4. Output using .format()
print("\n----- Library Audit Report -----")
print("Total Members with Late Fees: {}".format(len(Late_Fee_Members)))
print("Final Uppercase Audit Code: {}".format(Final_Code))
print("Late Fee Members: {}".format(Late_Fee_Members))
