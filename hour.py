c=list(map(int,input().split()))
d=list(map(int,input().split()))
x=c[0]*60+c[1]
y=d[0]*60+d[1]
k=abs(x-y)
print(str(k//60)+" "+str(k%60))
