import csv

with open('avocado.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
#print(rows)

for i in range(len(rows)):
    row=rows[i]
    nrow=row.split(", ")
    print(nrow)

