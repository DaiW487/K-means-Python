import numpy as np
import matplotlib.pyplot as plt
import math

X=([0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],[0.403,0.237],[0.481,0.149],[0.437,0.211],[0.666,0.091],[0.243,0.267],
[0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],[0.593,0.042],[0.719,0.103],[0.359,0.188],[0.339,0.241],[0.282,0.257],
[0.748,0.232],[0.714,0.346],[0.483,0.312],[0.478,0.437],[0.525,0.369],[0.751,0.489],[.532,0.472],[0.473,0.376],[0.725,0.445],[0.446,0.459])



C1=list()
C2=list()
C3=list()

label=list()
for i in range(30):
    label.append(0)

u1=np.array([0.403,0.237])
u2=np.array([0.343,0.210])
u3=np.array([0.632,0.172])

for n in range(4):
    for i in range(30):
       D1=math.sqrt((X[i][0]-u1[0])**2+(X[i][1]-u1[1])**2)
       D2=math.sqrt((X[i][0]-u2[0])**2+(X[i][1]-u2[1])**2)
       D3=math.sqrt((X[i][0]-u3[0])**2+(X[i][1]-u3[1])**2)

       if D1<=D2 and D1<=D3:
              label[i]=1
       if D2<=D1 and D2<=D3:
              label[i]=2
       if D3<=D1 and D3<=D2:
              label[i]=3

    C1.clear()
    for i in range(30):
       if label[i]==1:
              C1.append(X[i])
             
    C2.clear()
    for i in range(30):
       if label[i]==2:
              C2.append(X[i])
              
    C3.clear()
    for i in range(30):
       if label[i]==3:
              C3.append(X[i])
              
    shape1=len(C1)
    xsum=0
    for i in range(shape1):
       xsum=xsum+C1[i][0]
    u1[0]=xsum/shape1
    ysum=0
    for i in range(shape1):
       ysum=ysum+C1[i][1]
    u1[1]=ysum/shape1

    shape2=len(C2)
    xsum=0
    for i in range(shape2):
       xsum=xsum+C2[i][0]
    u2[0]=xsum/shape2
    ysum=0
    for i in range(shape2):
       ysum=ysum+C2[i][1]
    u2[1]=ysum/shape2

    shape3=len(C3)
    xsum=0
    for i in range(shape3):
       xsum=xsum+C3[i][0]
    u3[0]=xsum/shape3
    ysum=0
    for i in range(shape3):
       ysum=ysum+C3[i][1]
    u3[1]=ysum/shape3
