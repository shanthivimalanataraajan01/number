n=(input(""))
b=len(n)
a=['1','0']
c=0
for i in n:
    if i in a:
        c=c+1
if c==b:
    print("yes")
else:
    print("no")
   
