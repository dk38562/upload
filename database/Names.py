alan = ("Name: Alan Pan", "Member Since: 03/23/07", "Email: alanpan23@gmail.com")
maria = ("Name: Maria Pan", "Member Since: 03/24/07", "Email: mariapan24@gmail.com")
martin = ("Name: Martin Novak", "Member Since: 11/12/19", "Email: novakomole@gmail.com")
members = {
  "1234567890": alan,
  "0987654321": maria,
  "1293045672": martin,
}
x = raw_input("enter phone number here ")
#print out the list
if type(members[x]) == tuple:
  for i in range(len(members[x])):
    print((members[x])[i])
else:
  print ("sorry in valid request")
