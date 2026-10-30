target = 7
nums = [2, 3, 1, 2, 4, 3]
left=0
current_sum=0
min_length=float("inf")
for right in range(len(nums)):
    current_sum+=nums[right]
    while current_sum>=target:
         current_length=right-left+1
         if current_length< min_length:
          

          min_length=current_length
         current_sum-=nums[left]  
         left+=1  
if min_length==float("inf"):
         print(0)
else:
         print(min_length)
                
              

