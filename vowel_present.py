s=input()
a=['a','e','i','o','u']
for i in s:
    if i in a:
        print('yes')
        break
else:
    print('no')
