# Simple variables aur plain code bina kisi 'def' function ke
nums = [2, 7, 11, 15]
target = 9

seen_map = {}  # Dictionary {number: index} store karne ke liye
result = []    # Final answer ke liye

for i in range(len(nums)):
    current = nums[i]
    complement = target - current  # Target tak pahunchne ke liye kitna chahiye
    
    # Check karo kya complement pehle se map mein hai?
    if complement in seen_map:
        result = [seen_map[complement], i]
        # Complement ka purana index map se nikala aur current index (i) liya,
        # phir dono ke indices ko milakar final result mein save kar diya.
        # seen_map[complement] ka jaadu:
        # Jab complement (jaise 2) banta hai, toh Python dictionary (seen_map) 
        # ke andar jaakar key '2' ko talaash karti hai, aur uske samne 
        # jo purana index (jaise 0) pada hota hai, usko nikal kar le aati hai!
        break # Answer mil gaya toh loop rok do
    else:
        seen_map[current] = i  # Agar nahi hai toh current number aur index save kar do

print(result)  
# Output: [0, 1]