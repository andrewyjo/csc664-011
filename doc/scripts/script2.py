import mysql.connector
import datetime
from datetime import datetime
import random
import numpy as np

def isEqual(x, y):
    if(x == y):
        print("Point to Point")
        return True
    else:
        return False

mydb = mysql.connector.connect(
  host="localhost",
  user="tester00",
  password="Grapefruit123!@#",
  database="smartmediainterface"
)
date_format = '%Y-%m-%d %H:%M:%S'

start_times = mydb.cursor()
#end_times = mydb.cursor()


start_times.execute("SELECT start_time, end_time FROM File")
#end_times.execute("SELECT end_time FROM File")

start_res = start_times.fetchall()
#end_res = end_times.fetchall()
start = []
end = []
dateList = []

for x in start_res:
    dateList.append(x[0])
    start.append((x[0], x[1]))

for y in start:
    print("\n", y[0],", ", y[1])
    print(isEqual(y[0],y[1]))



#dateList.sort(key=lambda date: datetime.strptime(str(date), date_format))
for w in dateList:
    print(w)

#dateList.sort(key=lambda date: datetime.strptime(str(date), date_format))
#print(dateList.sort())
k = 4
randomPoints = random.sample(dateList,k)

relativeList = []
for x in dateList:
   relativeList.append((randomPoints[0] - x, randomPoints[1] - x, randomPoints[2] - x, randomPoints[3] - x))

for y in relativeList:
    print(y)

print(len(relativeList))

for w in relativeList:
    relativeList.append(w)


# Step 4, assign the 1st point to the nearest cluster
# assign the subsequent points to its nearest cluster


relativeList2 = []
for x in relativeList:
    relativeList2.append(min(x))

for y in relativeList2:
    print(y)