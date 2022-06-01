first = raw_input("first word: ")
second = raw_input("second word: ")
x = 0
y = raw_input(first + " number: ")
z = raw_input(second + " number: ")
length = raw_input("length: ")
while x < int(length):
    output = ""
    x = x + 1
    if x % int(y) == 0:
        output = output + first
    if x % int(z) == 0:
        output = output + second
    if output == "":
        output = x
    print(output)
