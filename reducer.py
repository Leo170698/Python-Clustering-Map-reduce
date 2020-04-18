import sys
import statistics as stats
import os
import numpy
i=0
for line in sys.stdin:
    line = line.strip()
    if i==0:
        centroids=line.split()
        centroids=list(map(float, centroids))
    elif(i==1):
        centroid1=line.split()
        centroid1=list(map(float, centroid1))
    elif(i==2):
        centroid2=line.split()
        centroid2=list(map(float, centroid2))
    elif(i==3):
        centroid3=line.split()
        centroid3=list(map(float, centroid3))
    i=i+1
cent1=stats.mean(centroid1)
cent2=stats.mean(centroid2)
cent3=stats.mean(centroid3)
if(numpy.isclose(centroids[0], cent1, rtol=1e-05, atol=1e-08, equal_nan=False) and numpy.isclose(centroids[1], cent2, rtol=1e-05, atol=1e-08, equal_nan=False) and numpy.isclose(centroids[1], cent2, rtol=1e-05, atol=1e-08, equal_nan=False)):
    print("The Centroid:",cent1)
    print("It's cluster:",centroid1)
    print("The Centroid:",cent2)
    print("It's cluster:",centroid2)
    print("The Centroid:",cent3)
    print("It's cluster:",centroid3)
else:
    print("iteration2")
    print(centroid1)
    print(centroid2)
    print(centroid3)
    with open("val.txt") as f:
        lines = f.readlines()
    lines[0] = str(cent1)+" "+str(cent2)+" "+str(cent3)+"\n"
    with open("val.txt", "w") as f:
        f.writelines(lines)
    os.system("type val.txt | python mapper.py | python reducer.py")





print(centroid1)
print(centroid2)
print(centroid3)
