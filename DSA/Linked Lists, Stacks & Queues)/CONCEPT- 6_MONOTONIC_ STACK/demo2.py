#(Largest Rectangle in Histogram - LC 84)#
def largestRectangleArea(heights):
    stack = []          # Indices store karega (heights increasing order mein)
    max_area = 0        # Ab tak ka sabse bara area
    heights_ext = heights + [0]  # Aakhir mein 0 taaki bache hue bars bhi pop hon

    for i, h in enumerate(heights_ext):
        # Jab current height  choti ho stack ke top bar ki height se,
        # toh top bar ke liye right boundary (i) mil gayi!
        while stack and h < heights_ext[stack[-1]]:
            mid_idx = stack.pop()              # Jis bar ka area nikalna hai
            bar_height = heights_ext[mid_idx]  # Uski height

            # Agar stack abhi bhi khali nahi hai, toh stack[-1] left boundary se just pehle ka index hai.
            # Agar stack khali ho gaya, toh bar shuru (index 0) se lekar i tak fail sakti hai.
            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1 

            area = bar_height * width
            if area > max_area:
                max_area = area

        # Current index i ko stack mein daal do
        stack.append(i)

    return max_area
# --- Local Testing ---
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([3, 1, 4, 2], 4),      # Naya test case
        ([4, 4, 4, 4], 16),     # Sab barabar heights
        ([5], 5),               # Single bar
    ]

    for idx, (bars, expected) in enumerate(test_cases, start=1):
        actual = largestRectangleArea(bars)
        status = "PASS" if actual == expected else "FAIL"
        print(f"Test {idx}: input={bars} | got={actual} | expected={expected} -> {status}")