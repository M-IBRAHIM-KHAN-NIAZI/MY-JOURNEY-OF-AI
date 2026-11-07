# LeetCode 3: Longest Substring Without Repeating Characters (chapter 3 ps / 3.py)
# (Dynamic sliding window aur set use karke duplicate characters track karte hain, 
# aur jab duplicate mile toh 'left' pointer se window shrink karke max length nikalte hain.)

s="abcabcbb"
left=0
chr_set=set()
max_length=0
for right in range(len(s)):
    while s[right] in chr_set:
        chr_set.remove(s[left])
        left+=1
    chr_set.add(s[right])   
    current_length=right-left+1
    if current_length>max_length:
        max_length=current_length
print(max_length)             