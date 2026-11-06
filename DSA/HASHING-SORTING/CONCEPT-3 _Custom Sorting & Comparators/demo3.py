from bisect import bisect_left

intervals = [[3, 4], [1, 2], [4, 5]]

# Step 1: Start times ko unke original index ke sath pack karo aur sort karo
starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
# Misaal ke taur par agar intervals = [[3, 4], [1, 2], [4, 5]] hain:
# 1. 'enumerate(intervals)' sabse pehle har interval ko ek index deta hai (jaise [3, 4] ko index 0).
# 2. '(interval[0], i)' har interval ka start time aur uska original index jod kar tuple banata hai, jaise: (3, 0).
# 3. 'for i, interval in ...' yeh kaam saare intervals par ek-ek karke chalata hai.
# 4. Aakhir mein 'sorted()' in saare tuples ko sirf pehli value (start time) ke hisab se chote se bada arrange kar deta hai: [(1, 1), (3, 0), (4, 2)]

# Step 2: Sirf sorted start times ki ek alag list nikal lo (Binary search ke liye)
start_times = [s[0] for s in starts]

res = []

# Step 3: Har interval ke end time ke liye right interval dhoondo
for interval in intervals:
    end_val = interval[1]
    
    # bisect_left se wo index dhoondo jahan start_time >= end_val ho
    idx = bisect_left(start_times, end_val)
    
    # Agar index valid range mein hai, to original index utha lo, warna -1
    if idx < len(starts):
        res.append(starts[idx][1])
        # Misaal ke taur par agar bisect_left se index ki value '2' aayi hai:
# 1. starts[idx] (yani starts[2]) list ke index 2 par jaakar wahan rakha hua poora tuple uthata hai, jaise: (4, 2).
# 2. Is tuple ke andar do values hoti hain: [0] par start time (4) aur [1] par original index (2).
# 3. Aakhri '[1]' is tuple ke andar se sirf original index ('2') ko nikal kar result mein save kar leta hai.
    else:
        res.append(-1)

print(res)