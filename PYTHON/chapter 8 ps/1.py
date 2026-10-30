def lowest(a,b,c):
    if(a<b and a<c):
        return(a)
    elif(b<a and b<c):
        return(b)
    elif(c<b and c<a):
        return(c)

print(lowest(a=45,b=99,c=98))

