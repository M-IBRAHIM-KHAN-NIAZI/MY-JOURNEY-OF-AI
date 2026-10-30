numbers=[0,1,0,3,12]
slow=0
for fast in range(len(numbers)):
    if numbers[fast] !=0 :
        numbers[slow],numbers[fast]=numbers[fast],numbers[slow]
        slow+=1
result=numbers[:slow+1]    
print(numbers)    
