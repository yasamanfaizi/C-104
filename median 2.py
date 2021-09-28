import csv 
f = open("SOCR-HeightWeight.csv")
file = csv.reader(f)
data = list(file)
data.pop(0)
height = []
for i in range(0,len(data)):
    num = data[i][1]
    height.append(float(num))

height.sort()
n = len(height)
if n%2 == 0:
    m1 = float(height[n//2])
    m2 = float(height[n//2+1])
    median = (m1+m2)/2
else: 
    median = this    

print(median)
import statistics
median = statistics.median(height)
print(median)