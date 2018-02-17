import csv
b = []
with open('./usd.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        b.append(float(row[0].replace("?","").replace(",","")))


resultFyle = open("out put.csv", 'w')

# Write data to file
for r in b:
    resultFyle.write(str(r) + "\n")
resultFyle.close()