while True:
    # valid query check:
    while True:
        goal = raw_input("Do you want to check a member or make a new entry? NewMem/Check ")
        if goal.lower() != "newmem" and goal.lower() != "check":
            print("invalid query")
        else:
            break
    if goal.lower() == "newmem":
        print(goal.lower())
    if goal.lower() == "check":
        alan = ("Name: Alan Pan", "Member Since: 03/23/07", "Email: alanpan23@gmail.com")
        maria = ("Name: Maria Pan", "Member Since: 03/24/07", "Email: mariapan24@gmail.com")
        martin = ("Name: Martin Novak", "Member Since: 11/12/19", "Email: novakomole@gmail.com")
        members = {
            "1234567890": alan,
            "0987654321": maria,
            "1293045672": martin,
        }
        x = raw_input("enter phone number here ")
        # print out the list
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
