##O Programa é lento mas chega lá
from random import randint
from statistics import stdev
def average(n):
    total=0
    for i in n:
        total+=i
    return total/len(n)
a=1
nNeedle=1000
resultList=[]

while (a>=0.005):
    #CODIGO
    resultList=[]
    for i in range(100):
        needleInCircle=0
        for i in range(nNeedle):
        
            x = randint(-100,100)/100
            y = randint(-100,100)/100
            if (x**2+y**2<=1):
                needleInCircle+=1
        resultList.append((4*needleInCircle)/nNeedle)
    #CODIGO
    a=stdev(resultList)
    nNeedle*=2
print("n needle",nNeedle)
print("std dev",a)
print("pi",average(resultList))