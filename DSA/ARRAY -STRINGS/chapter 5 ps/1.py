# LeetCode 344: Reverse String (chapter 5 ps / 1.py)
# (Two pointers use karke start aur end elements ko swap karte hain, 
# aur pointers ko center ki taraf move karke string ko in-place reverse karte hain.)

s = ["h", "e", "l", "l", "o"]
left=0
right=len(s)-1
while left<=right:
    s[left],s[right]=s[right],s[left]

    left+=1
    right-=1
print(f"reverse string is :{s}")    