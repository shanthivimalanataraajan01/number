n=int(input())

c=list(map(int,input().split()))
x=sorted(c)
for i in range(0,len(x)):
    if i==0:
        print(x[i],end="")
    else:
         print("",x[i],end="")
