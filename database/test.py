import datetime
import ast

date = datetime.datetime.now()
with open('numbers.txt') as f:
    data = f.read()
members = ast.literal_eval(data)
f.close()
while True:
    while True:
        num = raw_input("enter phone number here: ")
        if not num.isdigit():
            print("input has letters; try again")
        elif len(num) < 10:
            print("sorry that number is too short; try again")
        elif len(num) > 10:
            print("sorry that number is too long; try again")
        else:
            break
    try:
        print ("")
        for i in range(len(members[num])):
            print((members[num])[i])
        print ("")
    except:
        while True:
            goal = raw_input("Member not found; make a new member? yes/no ")
            if goal.lower() != "yes" and goal.lower() != "no":
                print("invalid query")
            else:
                break
        print ("work")
        if goal.lower() == "yes":
            name1 = raw_input("first name: ").title()
            name2 = raw_input("last name: ").title()
            mem = date.strftime("%x")
            email = raw_input("email: ")
            members[num] = (
            'Name: {} {}'.format(name1, name2), 'Member Since: {}'.format(mem), 'Email: {}'.format(email))
            f = open("numbers.txt", "w")
            f.write(str(members))
            f.close()
            print("")
            for i in range(len(members[num])):
                print((members[num])[i])
            print("")
