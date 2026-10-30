words=["donkey","good","bad","better"] 
with open("ibr.txt") as f:
    content=f.read()
    for word in words:
     content=content.replace(word,"#"*len(word))
    with open("ibr.txt","w")as f:
     f.write(content)
        




    


    