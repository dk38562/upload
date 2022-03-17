import datetime
import ast
date = datetime.datetime.now()
with open('numbers.txt') as f:
    data = f.read()
members = ast.literal_eval(data)
f.close()
while True:
    while True:
        goal = raw_input("Do you want to check a member or make a new entry? NewMem/Check ")
        if goal.lower() != "newmem" and goal.lower() != "check":
            print("invalid query")
        else:
            break
    if goal.lower() == "newmem":
        while True:
            num = raw_input("phone number: ")
            if not num.isdigit():
                print("input has letters; try again")
            elif len(num) < 10:
                print("sorry that number is too short; try again")
            elif len(num) > 10:
                print("sorry that number is too long; try again")
            else:
                break
        name1 = raw_input("first name: ").title()
        name2 = raw_input("last name: ").title()
        mem = date.strftime("%x")
        email = raw_input("email: ")
        members[num] = ('Name: {} {}'.format(name1, name2), 'Member Since: {}'.format(mem), 'Email: {}'.format(email))
        f = open("numbers.txt", "w")
        f.write(str(members))
        f.close()
        print("")
        for i in range(len(members[num])):
            print((members[num])[i])
        print("")
    if goal.lower() == "check":
        x = raw_input("enter phone number here ")
        print("")
        try:
            for i in range(len(members[x])):
                print((members[x])[i])
        except:
            if not x.isdigit():
                print("input has letters; try again")
            elif len(x) < 10:
                print("sorry that number is too short; try again")
            elif len(x) > 10:
                print("sorry that number is too long; try again")
            elif len(x) == 10:
                print("sorry that number is not in our system; try again")
            else:
                print("sorry invalid request; try again")
        print("")
