#Exercise 3

age=int(input("Enter your age: "))
adult_ticket=6.00
child_ticket=3.00
senior_citizen=2.00
if age < 16:
    print("Your ticket costs £",child_ticket)
elif age >=60:
    print("Your ticket costs £",senior_citizen)
else:
    print("Your ticket costs £",adult_ticket)
