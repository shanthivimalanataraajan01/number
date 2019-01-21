n=int(input())
s=input()
d=""
b=['a','e','i','o','u']
for i in s:
    if(i not in b):
        d=d+i
print(d[::-1])    
    
