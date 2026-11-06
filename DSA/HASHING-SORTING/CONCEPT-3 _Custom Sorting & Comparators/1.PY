                  #LeetCode 56: Merge Intervals (The Ultimate Classic)
intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
intervals.sort(key=lambda x:x[0])
merged=[]
for interval in intervals:

    if not merged or merged[-1][1] < interval[0]:
      
        
      merged.append(interval)
    else:
      merged[-1][1]=max(merged[-1][1],interval[1])

print(merged)
