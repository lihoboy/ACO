import numpy as np
alpha=1
beta=5
p=0.5

Q=100
P=100
file=open('TSP/Bays29.txt', 'r')
test = np.zeros((29,29), dtype=np.int)
test1 = np.zeros((Q,P), dtype=np.int)
#line = file.readlines()
#
i0=0
j0=0
# print(len(file))
# print(len(line[0]))
for i in file:
    print(i0)
    for n in i.split(' '):
        if n!='':
            test[i0][j0]=int(n)
            print(j0)
            j0+=1
    i0+=1
    j0 = 0


print (test[0][0])
print (test1)