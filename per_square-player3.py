import math
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
      d=math.sqrt(i)
      e=int(d)
      if e==d:
            c=c+1
print(c)            
