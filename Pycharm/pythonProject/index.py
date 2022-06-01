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
  print(goal.lower())
