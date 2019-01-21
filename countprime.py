def isprime(n):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
              return False
        else:
            return True



n,s=map(int,input().split())
c=0
for i in range(n,s+1):
    if isprime(i):
        c+=1
print(c) 
