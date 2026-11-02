nums = [2, 7, 11, 15]
target = 9
left = 0
right = len(nums) - 1
result = []

while left < right:
    current_sum = nums[left] + nums[right]
    
    if current_sum == target:
        result = [left + 1, right + 1]
        break  # Yeh 'if' ke bilkul andar (neech wale block mein) hona chahiye
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(result)