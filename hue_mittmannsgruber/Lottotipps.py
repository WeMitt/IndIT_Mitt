import random

a=[0,0,0,0,0,0]

iversuche=int(input("Wieviel Tipps soll ich generieren?"))

for anzahl in range(0,iversuche):
    for i in range(0,6):
        a[i]=round(random.random()*44+1)
        for j in range(0,i):
            while a[i]==a[j]:
                #print("Retry",a[i])
                a[i]=round(random.random()*44+1)
    print(a)
