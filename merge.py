def mergeSort(a):

  if len(a)>1:
        mid = len(a)//2
        b = a[:mid]
        c = a[mid:]

        mergeSort(b)
        mergeSort(c)

        i=0
        j=0
        k=0
        while i < len(b) and j < len(c):
            if b[i] < c[j]:
                a[k]=b[i]
                i=i+1
            else:
                a[k]=c[j]
                j=j+1
            k=k+1

        while i < len(b):
            alist[k]=b[i]
            i=i+1
            k=k+1

        while j < len(c):
            alist[k]=c[j]
            j=j+1
            k=k+1
    print(a)
n=int(input())
a = list(map(int,input().split()))
mergeSort(a)
print(a)
