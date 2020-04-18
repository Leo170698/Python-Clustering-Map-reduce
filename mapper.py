import sys
i=0
all=[]
cent1=[]
cent2=[]
cent3=[]

for line in sys.stdin:
    line = line.strip()
    if i==0:
        centroids=line.split()
    else:
        values=line.split()
    i=i+1


#---------------------------------------#
for cent in centroids:
    centname=cent
    centname=[]

    for val in values:
        diff = abs(float(cent)-float(val))
        centname.append([float(cent),diff])
    all.append(centname)





for i in range(0,len(values)):
    if (all[0][i][1] < all[1][i][1] and all[0][i][1] < all[2][i][1]):
        cent1.append(values[i])

    elif(all[1][i][1] < all[0][i][1] and all[1][i][1] < all[2][i][1]):
        cent2.append(values[i])
    elif(all[2][i][1] < all[0][i][1] and all[2][i][1] < all[1][i][1]) :
        cent3.append(values[i])
for i in centroids:
     print(i,end = " ")
print("\t")
for i in cent1:
     print(i,end = " ")
print("\t")
for i in cent2:
     print(i,end = " ")
print("\t")
for i in cent3:
     print(i,end = " ")
