class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [30,38,30,36,35,40,28]
        stack = []
        out = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([i, v])
                continue
            
            while len(stack) != 0 and v > stack[-1][1]:
                stacki, stackv = stack.pop()
                out[stacki] = i - stacki

            stack.append([i, v])
            

        return out




