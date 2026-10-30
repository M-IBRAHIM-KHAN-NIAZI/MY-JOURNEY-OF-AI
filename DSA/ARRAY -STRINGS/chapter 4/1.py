def build_prefix_sum(nums):
    # Step 1: Utni hi lambi aik empty list bana li jismein sab jagah 0 ho
    prefix = [0] * len(nums)
    
    # Step 2: Pehla element hamesha same rehta hai kyunki uske pehle kuch nahi hota
    prefix[0] = nums[0]
    
    # Step 3: Loop chalaya index 1 se lekar aakhri element tak
    for i in range(1, len(nums)):
        # Yahan wahi formula lag raha hai jo tune socha hai:
        # Pichhla total sum (prefix[i-1]) + Original list ka current element (nums[i])
        prefix[i] = prefix[i - 1] + nums[i]
        
    return prefix

# Test the function
nums = [1, 4, 8, 2]
print(build_prefix_sum(nums))  # Output: [1, 5, 13, 15]



