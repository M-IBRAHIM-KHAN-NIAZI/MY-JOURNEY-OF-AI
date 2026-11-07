# LeetCode 643: Maximum Average Subarray I (chapter 3 ps / 1.py)
# (Fixed sliding window technique use karke pehle 'k' elements ka sum lete hain, 
# phir window slide karke max sum update karte hain aur end mein average nikalte hain.)

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

