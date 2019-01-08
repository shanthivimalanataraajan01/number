n=int(input(""))
b=n
a=0
while(n>0):
    r=n%10
    a=a+r*r*r
    n=n//10
print(a)
if b==a:
    print("yes")
else:
    print("no")
