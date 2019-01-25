a=input()
c=len(a)//2
d=list(a)

for i in range(len(d)):
    if len(a)%2==0:
        d[c-1],d[c]="*","*"
    else:
        d[c]="*"
for i in d:
    print(i,end="")
