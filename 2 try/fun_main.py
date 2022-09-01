def personal_details():
    # name, dateOfJoin = "Simon", 19
    name = input("Enter the Learner Name")
    dateOfJoin = input("Enter the Date which you Acedmy Join")

    Duration = input("Enter the Duration of Learning that you want")
    EorF = input("Are you Experienced or fresher")
    Id = input("Enter the User ID")
    TypeOfDance = input("Enter the Type of Dance which you want")

    while True:
        ExprOrFresher = input("Are you Fresher or Experienced?")
        if ExprOrFresher == ("Fresher"):
            print(name+" "+ "is Fresher")
        else:
            print(name+" "+ "is Experienced")
        break
    print("Name: {}\nDate of Join: {}\nDuration: {} \nEorF: {} \nId: {} \nTypeOfDance: {}".format(name, dateOfJoin, Duration, EorF, Id , TypeOfDance))

personal_details()

user_list = []

print("\n")
for i in range(0, 1):
    item = input("Enter the Learner Name")
    item = input("Enter the Date which you Acedmy Join")
    item = input("Are you Experienced or fresher")
    item = input("Enter the Duration of Learning that you want")
    item = input("Enter the User ID")
    item = input("Enter the Type of Dance which you want")

    user_list.append(item)

user_list.append(item)

