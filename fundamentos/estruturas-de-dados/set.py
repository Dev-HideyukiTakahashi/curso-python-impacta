#set não permite repetição de valores

s = set()
s.add(1)
s.add(12)
print(s)

#output: {1, 12}

s.add(12)
print(s)

#output: {1, 12}
