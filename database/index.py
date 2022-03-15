import ast
with open('numbers.txt') as f:
    data = f.read()
members = ast.literal_eval(data)
while True:
    while True:
        goal = raw_input("Do you want to check a member or make a new entry? NewMem/Check ")
        if goal.lower() != "newmem" and goal.lower() != "check":
            print("invalid query")
        else:
            break
    if goal.lower() == "newmem":
        print(goal.lower())
    if goal.lower() == "check":
        x = raw_input("enter phone number here ")
        try:
            for i in range(len(members[x])):
                print((members[x])[i])

        except:
            if x.isdigit() == False:
                print ("input has letters; try again")
            elif len(x) < 10:
                print ("sorry that number is too short; try again")
            elif len(x) > 10:
                print ("sorry that number is too long; try again")
            elif len(x) == 10:
                print("sorry that number is not in our system; try again")
            else:
                print ("sorry invalid request; try again")
        print ("")
