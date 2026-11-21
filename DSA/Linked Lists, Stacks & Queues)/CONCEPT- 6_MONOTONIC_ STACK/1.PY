###(Daily Temperatures - LC 739) ###
class solution:
    def temp(self,temperatures):
        n=len(temperatures)
        stack=[]
        result=[0]*n

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_temp=stack.pop()
                result[prev_temp]=i-prev_temp

            stack.append(i)    
        return result    

if __name__ == "__main__":
    sol = solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.temp(temps))  # [1, 1, 4, 2, 1, 1, 0, 0]   
