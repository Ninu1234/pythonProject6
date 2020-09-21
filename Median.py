import csv
with open('height-weight.csv',newline = '')as f:
    reader = csv.reader(f)
    fileData = list(reader)
###print(fileData)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))
n = len(newData)
print(n)
newData.sort()
if n % 2 == 0:
    median1 = float(newData[n//2])
    print(median1)
    median2 = float(newData[n//2 -1])
    print(median2)
    median = (median1+median2)/2
else:
    median = float(newData[n//2])
print(median)