import csv;
f = open("SOCR-HeightWeight.csv",newline='')
read_data = csv.reader(f)
all_data = list(read_data)
all_data.pop(0)
newdata = []
for i in range(len(all_data)):
    num = all_data[i][1]
    newdata.append(float(num))
new_data = len(newdata)
total_number = 0
for a in newdata:
    total_number = total_number+a
average = total_number/new_data
print("the Average is-> "+str(average))