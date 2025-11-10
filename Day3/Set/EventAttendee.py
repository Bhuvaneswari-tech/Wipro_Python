'''
Scenario: Event Attendee Management

Description:
A company is organizing a tech conference. They want to manage the list of 
registered attendees using a set, because each attendee should be unique 
(no duplicates).

The system should be able to:

Add new attendees who register.
Remove attendees who cancel their registration.
Check if an attendee is registered.
Combine lists of attendees from multiple events.
Find common attendees between two events.

'''

#Event A and Event B attendees
event_a = {"Alice",'Bob','Charlie','Diana'}
event_b = {'Charlie','Eve','Frank','Alice'}

#Add a new attendee "George" to Event A
event_a.add("George")
print("Event A after adding George: ",event_a)

#Remove attendee Bob from Event A
event_a.remove("Bob")
print("Event A after removing Bob: ",event_a)

#Check if "Eve" is registered Event A
is_registered = "Eve" in event_a
print("Is Eve registered in Event A?",is_registered)

#Combine attendees from Event A and Event B
all_attendees = event_a.union(event_b)
print("All attendees from both events:",all_attendees)

#Find attendees who registered for both events
common_attendees = event_a.intersection(event_b)
print("Attendees in both events:",common_attendees)

set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}
set4 = {7,8,9}

result = set1.union(set2,set3,set4)

result1 = set1 | set2 | set3 | set4