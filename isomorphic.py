s,r=map(str,input().split())
l=[]
k=[]
c=0
if len(s)==len(r):
    for i in s:
        a=s.count(i)
        l.append(a)
    for j in r:
        b=r.count(j)
        k.append(b)
    for m in range(0,len(l)):
        for n in range(0,len(k)):
            if m==n:
                if l[m]==k[n]:
                    c+=1
    if c==len(l):
        print("yes")
    else:
        print("no")
else:
    print("no")

