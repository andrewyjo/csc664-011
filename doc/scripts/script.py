# Event Based Time Clustering

import mysql.connector
import datetime
from datetime import datetime
import random

def isEqual(x, y):
    if(x == y):
        print("Point to Point")
        return True
    else:
        return False
    
def getMinIndex(relativeList):

    min_value = min(relativeList)
    min_index = []
    index = 0
    for i in range(0, len(relativeList)):
        if min_value == relativeList[i]:
            min_index.append(i) 
            #index+=1
    return min_index
    

def findNearestCluster(index, randomPoints, dateList):

    relativeList = []
    for x in randomPoints:
        relativeList.append(x - dateList[index])
    print(relativeList)
    # Step 4) Assign the 1st point to the nearest cluster
    
    #Find Nearest Cluster
    min_index = getMinIndex(relativeList)
    #nearestPoint = []
    #nearestPoint.append(min_index)
    return min_index


def stepFour(dateList, randomPoints):
    relativeList = []
    index = 0
    index2 = 0
    nearestList = []

    for x in dateList:
        for y in randomPoints:
            relativeList.append(y - dateList[index])
        index+=1
        min_index = getMinIndex(relativeList)
        print(max(min_index))
        nearestList.append(min_index)
        relativeList.clear

    return nearestList

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

#print(dateList[200]-dateList[0])
#K-Means Clustering
#k = 4
# Step 1) Select K
k = 4
# Step 2) Randomly select 3 data points
randomPoints = random.sample(dateList,k)

#for i in range(0, len(dateList)):
#    q = findNearestCluster(i, randomPoints, dateList)
#    print(q)

# Step 3) Measure the distance between the 1st point and the 3 initial clusters

relativeList = []
index = 0
index2 = 0




# for x in dateList:
#     for y in randomPoints:
#         relativeList.append(y - dateList[index])
#     index+=1
#     min_index = getMinIndex(relativeList)
#     print(max(min_index))
#     relativeList.clear


# print(stepFour(dateList, randomPoints))

    


    

#def stepFour(dateList, randomPoints):
#    relativeList = []
#    index = 0
#    index2 = 0
#    nearestList = []
#
#    for x in dateList:
#        for y in randomPoints:
#            relativeList.append(y - dateList[index])
#        index+=1
#        min_index = getMinIndex(relativeList)
#        #print(max(min_index))
#        nearestList.append(max(min_index))
#        relativeList.clear

#for x in randomPoints:
#    relativeList.append(x - dateList[index])
#    index+=1
##print(relativeList)
#print(index)
#getMinIndex(relativeList)
#assignedPoints = []
#for y in dateList:
#    while(index < len(dateList)):
#        for x in randomPoints:
#            relativeList.append(x - dateList[index])
#        getMinIndex(relativeList)
#        index+=1
#        relativeList.clear()


#index2 += 1
#print("index2:", index2)



# Step 4) Assign the 1st point to the nearest cluster

#Find Nearest Cluster

#min_index = getMinIndex(relativeList)
#nearestPoint = []
#nearestPoint.append(min_index)
#relativeList = []

#index = 0
#min_value = min(relativeList)
#min_index = []
#for i in range(0, len(relativeList)):
#    if min_value == relativeList[i]:
#        print(i)
#        #min_index.append(i)

    








# Step 5) Calculate the mean of each cluster


# Step 6) Repeat
