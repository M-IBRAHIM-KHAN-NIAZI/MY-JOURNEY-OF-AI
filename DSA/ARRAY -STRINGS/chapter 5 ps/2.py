# LeetCode 242: Valid Anagram (chapter 5 ps / 2.py)
# (Hash maps / frequency dictionaries use karke dono strings ke characters ki counts match karte hain, 
# aur agar frequencies identical hon toh True return hota hai.)

s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print(False)
else:
     s_freq={}
     t_freq={}

     for char in s:
       s_freq[char]=s_freq.get(char,0)+1
     for char in t:
       t_freq[char]=t_freq.get(char,0)+1 
        

     if s_freq==t_freq:
          print(True)
     else:
          print(False)    