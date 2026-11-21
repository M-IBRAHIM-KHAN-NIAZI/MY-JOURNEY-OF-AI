
###(Daily Temperatures - LC 739) ###
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of days waiting for a warmer day

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day #basically jo
            stack.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temps))  # [1, 1, 4, 2, 1, 1, 0, 0]