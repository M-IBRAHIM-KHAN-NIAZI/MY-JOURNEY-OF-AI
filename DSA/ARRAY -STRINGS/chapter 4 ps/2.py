nums = [1, 7, 3, 6, 5, 6]
total_nums=sum(nums)

def pivotindex(nums):
    left_sum=0
    for i in range(len(nums)):
        right_sum=total_nums - left_sum - nums[i]

        if right_sum==left_sum:
            return i
        left_sum+=nums[i]
    return -1

print(f'total sum of nums is : {total_nums}')
print(f"the pivot index is : {pivotindex(nums)} ")