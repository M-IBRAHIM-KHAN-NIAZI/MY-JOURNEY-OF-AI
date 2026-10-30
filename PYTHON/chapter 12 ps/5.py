n=int(input("enter your number:"))

multiplerlist=[i*n for i in range(1,11)]
print(multiplerlist)


with open("tables.txt","a") as f:
    f.write(str(multiplerlist)+ "\n")

