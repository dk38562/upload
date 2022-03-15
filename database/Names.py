import ast
with open('numbers.txt') as f:
    data = f.read()
members = ast.literal_eval(data)
x = raw_input("name ")
members[3] = x