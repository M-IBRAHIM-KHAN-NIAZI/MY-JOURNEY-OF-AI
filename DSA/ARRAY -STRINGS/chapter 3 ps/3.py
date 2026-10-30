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