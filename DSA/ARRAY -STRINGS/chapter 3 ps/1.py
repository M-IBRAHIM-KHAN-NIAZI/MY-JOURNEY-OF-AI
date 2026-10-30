nums = [1, 12, -5, -6, 50, 3]
k = 4
current_sum=sum(nums[:k])
max_sum=current_sum

for i in range(k,len(nums)):
    current_sum=current_sum-nums[i-k]+nums[i]
    if current_sum> max_sum:
        max_sum=current_sum
result=max_sum/k
print(result)

