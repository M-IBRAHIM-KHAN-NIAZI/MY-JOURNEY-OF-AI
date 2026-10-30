a=[1,1,3,3,5,6,7,7]
slow=0
for fast in range(1,len(a)):
    if a[fast]!=a[slow]:
        slow+=1
        a[slow]=a[fast]
result=a[:slow+1]
print(result)

