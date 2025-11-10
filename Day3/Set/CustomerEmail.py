'''
Scenario
An online store wants to store unique customer emails for sending promotional 
offers. Email should not repeat
'''

#Initial set of customer emails
emails = {"alice@example.com","bob@example.com","alice@example.com","charlie@example.com"}
#print(emails)

#Add a new customer
emails.add("diana@example.com")

#Remove a customer email
emails.remove("bob@example.com")

#check if an email is registered
print("Is charlie@example.com registered?", "charlie@example.com" in emails)

#List all registered emails
print("Registered Emails:",emails)