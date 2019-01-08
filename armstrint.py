def isarmstrong(n):
     b=n
     a=0
     while(n>0):
        r=n%10
        a=a+r*r*r
        n=n//10
     if b==a:
         return True
     else:
         return False

n,s=map(int,input().split())

c=0
for i in range(n+1,s):
    if isarmstrong(i):
        if c==0:
           print (i,end="")
           c=c+1
        else:
           print("",i,end="")
