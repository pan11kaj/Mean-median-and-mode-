import csv;
f = open("SOCR-HeightWeight.csv",newline='')
read_data = csv.reader(f)
all_data = list(read_data)
all_data.pop(0)
newdata = []
for i in range(len(all_data)):
    num = all_data[i][1]
    newdata.append(float(num))
n = len(newdata)
newdata.sort()
if n%2 == 0:
    m1 = float(newdata[n//2])
    m2 = float(newdata[n//2-1])
    median = (m2+m1)/2
else:
    median = newdata[n//2]
print("the median is: "+str(median))