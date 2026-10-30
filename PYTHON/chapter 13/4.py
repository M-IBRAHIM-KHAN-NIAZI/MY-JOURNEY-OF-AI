# map example
from functools import reduce
l=[1,2,3,4,5,6]
sqlist=lambda x: x*x
p=map(sqlist,l)
print(list(p))

# filter example
def even(n):

    if(n%2==0):
        return True
    return False
evenlist=filter(even,l)
print(list(evenlist))
# reduce example
def sum(a,b):
    return a+b
print(reduce(sum,l))