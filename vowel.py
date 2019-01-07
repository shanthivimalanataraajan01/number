s=input("")
if (s=="a" or s=="e" or s=="i" or s=="o" or s=="u"):
    print("Vowel")
elif(ord(s)>=97 and ord(s)<=122):
    print("Consonant")
else:
    print("invalid")
