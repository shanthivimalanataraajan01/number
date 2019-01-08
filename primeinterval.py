def isprime(n):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
              return False
        else:
            return True



n,s=map(int,input().split())
c=0
for i in range(n+1,s):
    if isprime(i):
        if c==0:
           print (i,end="")
           c=c+1
        else:
           print("",i,end="")
