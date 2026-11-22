#(Largest Rectangle in Histogram - LC 84)#
def largest_rectangle_area(heights):
    stack=[]
    heights_ext=heights + [0]
    max_area=0
    for i,h in enumerate(heights_ext):
        while stack and h < heights_ext[stack[-1]]:
            mid_idx=stack.pop()
            bar_height=heights_ext[mid_idx]

            left_boundary= stack[-1] if stack else -1
            width=i-left_boundary-1
            Area=width * bar_height
            if Area > max_area:
                max_area=Area
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
        actual = largest_rectangle_area(bars)
        status = "PASS" if actual == expected else "FAIL"
        print(f"Test {idx}: input={bars} | got={actual} | expected={expected} -> {status}")
