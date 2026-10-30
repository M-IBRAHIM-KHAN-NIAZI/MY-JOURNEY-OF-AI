# Yahan humne input variable 's' shuru mein hi define kar diya hai
s = "A man, a plan, a canal: Panama"

# Step 1: Pointers ko initialize karo
left = 0
right = len(s) - 1

is_palindrome = True

# Step 2: Jab tak left pointer right se chota hai, loop chalega
while left < right:

  # Step 3: Agar left pointer par koi aisi cheez hai jo letter ya number nahi hai (jaise space ya comma), toh use skip karo aur left ko aage barha do
  while left < right and not s[left].isalnum():
    left += 1

  # Step 4: Agar right pointer par koi aisi cheez hai jo letter/number nahi hai, toh use skip karo aur right ko peechhe le aao
  while left < right and not s[right].isalnum():
    right -= 1

  # Step 5: Ab dono taraf valid characters hain, unhein lowercase karke aapas mein compare karo
  if s[left].lower() != s[right].lower():
    is_palindrome = False
    break  # Agar match nahi hue, toh loop wahin tod do kyunki palindrome nahi hai

  # Step 6: Agar match ho gaye, toh dono pointers ko andar ki taraf move karo
  left += 1
  right -= 1

# Step 7: Final result print karo
print(is_palindrome)