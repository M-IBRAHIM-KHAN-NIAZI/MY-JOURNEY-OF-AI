from collections import deque


def maxSlidingWindow(nums, k):
    dq = deque()  # Indices store karega (values decreasing order mein)
    result = []

    for i in range(len(nums)):
        # 1. Jo index window [i - k + 1, i] se bahar chala gaya, use front se hatao
        if dq and dq[0] <= i - k: # basically eska matlab ye ha ke agr ye condition true hoyi tu element window size se  
           # bahar nikal  chuka ha
            dq.popleft()

        # 2. Current element se chote ya barabar elements back se hatao
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        # 3. Current index ko back mein daalo
        dq.append(i)

        # 4. Jab pehli poori window ban jaye (i >= k - 1), front ka element max hai
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


#Simple local testing
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(maxSlidingWindow([1], 1))                          # [1]
print(maxSlidingWindow([4, 2, 1], 2))                    # [4, 2]