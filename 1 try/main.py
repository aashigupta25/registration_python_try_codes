'''Registration Form'''
from operator import itemgetter

registration = {}

for i in range(4):
    name = input("Enter Candidate's name: ")
    dateOfJoin = input("Enter Date of joining date: ")

    registration[name] = dateOfJoin

print(registration)

# Show Entries
print(registration.items())

N_DOJ = [(name, dateOfJoin) for name, dateOfJoin in registration.items()]
print(N_DOJ)

while True:
    ExprOrFresher = input("Are you Fresher or Experienced?")
    if ExprOrFresher == ("Fresher"):
        print(name+" "+ "is Fresher")
    else:
        print(name+" "+ "is Experienced")
    break

learning_duration = input("What is Your Learning Duration in the month?")
print(learning_duration)

ID = input("Enter Your Id?")
print(ID)


# Show specific details
b = registration.keys()
print(b)

ps = [("Name1", "opp"), ("Name2", "tyu"), ("Name3", "dedfw"), ("Name4", "adfew"), ("Name5", "df")]
got = itemgetter(0, 2, 3)(ps)
print(got)

# Filter for Dance form
list1 = ['Khatak', 'Hiphop', 'kucipudi', 'Westren', 'Freestyle', 'bharatnatyam']
list2 = []
n = input("Enter the Dance form which you want to learn: ")
for i in range(1):
    ele = input("Enter the Dance form which you want to learn:")
    list2.append(ele)
filter_data = [x for x in list2 if all(y not in x for y in list1)]
print("The Dance forms which we teach us:", list1)
print("The Dance form which you want to learn:", list2)
print("Happy Learning:", filter_data)

# Filter for Dates and Duration
