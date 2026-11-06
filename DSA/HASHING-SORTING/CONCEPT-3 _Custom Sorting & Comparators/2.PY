                                  ## LeetCode 436: Find Right Interval##
from bisect import bisect_left

intervals = [[3, 4], [1, 2], [4, 5]]

starts=sorted((interval[0],i)for i,interval in enumerate(intervals))

starts_time=[s[0] for s in starts]
result=[]

for interval in intervals:
    end_value=interval[1]
    index=bisect_left(starts_time,end_value)

    if index<len(starts_time):
        result.append(starts[index][1])
    else:
        result.append(-1)
print(result)            





