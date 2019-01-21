s=input()
b=[]
for j in range(0,len(s)):
    b.append(j)
a=""
for i in range(0,len(b),2):
    b[i],b[i+1]=b[i+1],b[i]
    a=a+b[i]+b[i+1]
print(a)    
    
