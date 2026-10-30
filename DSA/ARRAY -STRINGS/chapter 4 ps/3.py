# Inputs
nums = [1, 1, 1]
k = 2

# Variables
total_subarrays = 0         # Final counter
current_sum = 0             # Running prefix sum

# Diary / Hash Map: {prefix_sum: frequency}
prefix_counts = {0: 1}      # Base case

# Logic Loop (Tumhara same pehle wala indexing tareeqa)
for i in range(len(nums)):
    # 1. Index i ki value se current sum update kiya
    current_sum += nums[i]
    
    # 2. Formula: Konsa pichhla sum chahiye?
    required_previous_sum = current_sum - k
    
    # 3. Diary mein check karo
    if required_previous_sum in prefix_counts:
        total_subarrays += prefix_counts[required_previous_sum]
        
    # 4. Current sum ko diary mein store / update karo
    if current_sum in prefix_counts:
        prefix_counts[current_sum] += 1
    else:
        prefix_counts[current_sum] = 1

# Output
print("Total Subarrays Found:", total_subarrays)
