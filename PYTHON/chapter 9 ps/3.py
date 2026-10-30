word="donkey"
with open("ibr.txt") as f:
    content=f.read()
    contentnew=content.replace(word,"######")
    with open("ibr.txt","w")as f:
        f.write(contentnew)

