f = open(__file__, 'r')
list_of_lines = list()
for line in f:
    list_of_lines.append(line[::-1])
for line in list_of_lines[::-1]:
    print(line, end="")
f.close()
