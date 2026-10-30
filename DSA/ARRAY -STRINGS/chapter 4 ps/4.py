nums=[1,1,1,]
k=2
total_subarrays=0
current_sum=0

prefix_count={0:1}
for i in range(len(nums)):
    current_sum+=nums[i]
    required_previous_sum=current_sum - k
    if required_previous_sum in prefix_count:
        total_subarrays+=prefix_count[required_previous_sum]
    if current_sum in prefix_count:
        prefix_count[current_sum]+=1
    else:
        prefix_count[current_sum]=1

print(f"your total subarrays is : {total_subarrays}")