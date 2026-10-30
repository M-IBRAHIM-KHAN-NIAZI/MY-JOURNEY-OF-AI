s = ["h", " ", "e", "l", "l", "o"]

slow = 0

for fast in range(len(s)):
  if s[fast] != " ":
    s[slow] = s[fast]
    slow += 1

result = s[:slow+1]
print(result)

