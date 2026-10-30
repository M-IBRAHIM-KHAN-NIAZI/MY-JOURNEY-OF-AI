nums = [-2, 0, 3, -5, 2, -1]
prefix=[0]*len(nums)
prefix[0]=nums[0]
for i in range (1,len(nums)):
    prefix[i]=prefix[i-1]+nums[i]
def sum_range(left,right):
    if left==0:
        return prefix[right]
    return prefix[right]-prefix[left-1]

print(f"original nums : {nums}" ) 
print(f"orignal prefix sum: {prefix}")
print(f"prefix sum from index 1 to 4 is: {sum_range(1,4)}")