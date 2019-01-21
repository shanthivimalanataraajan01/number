s=input()
a=['#','@','$','%','_','&','*','.','!']
c=0
for i in s:
    if i in a:
        c=c+1
print(c)        
