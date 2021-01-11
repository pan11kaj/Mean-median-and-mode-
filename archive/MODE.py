import csv;
from collections import Counter;
f = open("SOCR-HeightWeight.csv",newline='')
read_data = csv.reader(f)
all_data = list(read_data)
all_data.pop(0)
newdata = []
for i in range(len(all_data)):
    num = all_data[i][1]
    newdata.append(float(num))
data = Counter(newdata)
setModeforrang={
                "75-85":0,
                "85-95":0,
                "95-105":0,
                "105-115":0,
                "115-125":0,
                "125-135":0,
                "135-145":0,
                "145-155":0,
                "155-165":0,
                "165-175":0,
}
for height,occ in data.items():
    if 75<float(height)<85:
        setModeforrang["75-85"]+=occ
    elif 85<float(height)<95:
        setModeforrang["85-95"]+=occ
    elif 95<float(height)<105:
        setModeforrang["855-105"]+=occ
    elif 105<float(height)<115:
        setModeforrang["105-115"]+=occ
    elif 115<float(height)<125:
        setModeforrang["115-125"]+=occ
    elif 125<float(height)<135:
        setModeforrang["125-135"]+=occ
    elif 135<float(height)<145:
        setModeforrang["135-145"]+=occ
    elif 145<float(height)<155:
        setModeforrang["145-155"]+=occ
    elif 155<float(height)<165:
        setModeforrang["155-165"]+=occ
    elif 165<float(height)<175:
        setModeforrang["165-175"]+=occ
mode_range,mode_occurence = 0,0
for range,occ in setModeforrang.items():
    if occ>mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occ
        mode = float((mode_range[0]+mode_range[1])/2)
print(f"mode is-> {mode:2f}")