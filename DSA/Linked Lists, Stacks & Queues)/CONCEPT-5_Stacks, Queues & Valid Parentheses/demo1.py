#LEET CODE 20:VALID BRACKETS
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping banate hain closing aur opening brackets ki
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # Agar character closing bracket hai
            if char in mapping:
                # Stack ka top nikal lo ya delete kardo ya agar stack khali hai toh dummy value de do
                top_element = stack.pop() if stack else '#'
                
                # Check karo kya woh matching opening bracket hai
                if mapping[char] != top_element:
                    return False
            else:
                # Agar opening bracket hai, toh stack mein push kar do
                stack.append(char)
                
        # Agar aakhir mein stack bilkul khali hai, toh True, warna False
        return not stack


# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 '()[]{{}}' (Expect True): {sol.isValid('()[]{}')}")
    print(f"Test 2 '(]' (Expect False): {sol.isValid('(]')}")
    print(f"Test 3 '([)]' (Expect False): {sol.isValid('([)]')}")