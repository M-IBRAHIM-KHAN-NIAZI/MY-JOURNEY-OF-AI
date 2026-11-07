# LeetCode 724: Find Pivot Index (chapter 4 ps / 2.py)
# (Pehle poore array ka total sum nikalte hain, phir loop chala kar left sum aur 
# right sum compare karte hain, aur jahan dono equal ho jayein woh pivot index return hota hai.)

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