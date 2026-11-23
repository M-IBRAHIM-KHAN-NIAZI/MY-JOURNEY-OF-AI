# Sliding Window Maximum (LeetCode 239)
#Tumhara kaam bas itna hai:
#nums ke upar k size ki ek chashma/window rakho, usay left se right slide karte jao, aur har window ke andar jo sabse bara
# number nazar aaye, usay ek list (result) mein likhte jao.
from collections import deque

def maxSlidingWindow(nums, k):
    dq=deque()
    result=[]

    for i in range(len(nums)):
        if dq and dq[0]<=i-k:# Check karta hai ke front wala index (dq[0]) window ke size se bahar nikal gaya ya nahi
# Agar dq[0] <= i - k aata hai toh woh expired ho chuka hai, isliye left side se popleft() kar dete hain
            dq.popleft()

        while dq and nums[dq[-1]]<=nums[i]:# Check karta hai ke deque ke end (dq[-1]) par pare index ki value 
            #current nums[i] se choti ya barabar toh nahi
# Agar choti ya barabar hoti hai toh usay pop() karke hata dete hain kyunke naya bara element aage aa gaya hai
            dq.pop()

        dq.append(i)

        if i >= k-1:# Tab chalti hai jab k size ki poori window ban jati hai (i >= k - 1)
# Iske baad result mein front wale sabse bare element (nums[dq[0]]) ki value append kar dete hain
            result.append(nums[dq[0]])
    return result
                
#Simple local testing
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(maxSlidingWindow([2,1,5,3], 2))                          # [2,5,5]
print(maxSlidingWindow([4, 2, 1], 2))                    # [4, 2]
# Sliding Window aise kaam karti hai ke pehle 'k' size ki pehli window ban kar uske elements check kiye jaate hain;
# phir har agle step mein window ko aage saraktay hue left se purana element nikala jaata hai aur right se naya element add karke dubara check kiya jaata hai—
# is tarah poori array par bina dobara shuru se ghumay har window ka result nikal aata hai.
