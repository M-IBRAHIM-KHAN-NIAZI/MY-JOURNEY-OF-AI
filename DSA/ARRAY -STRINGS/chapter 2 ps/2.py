# LeetCode 283: Move Zeroes
# (Two pointers use karke non-zero elements ko aage shift karte hain 
# aur zeros ko end mein move kiya jata hai, in-place.)
numbers=[0,1,0,3,12]
slow=0
for fast in range(len(numbers)):
    if numbers[fast] !=0 :
        numbers[slow],numbers[fast]=numbers[fast],numbers[slow]
        slow+=1
result=numbers[:slow+1]    
print(numbers)    
