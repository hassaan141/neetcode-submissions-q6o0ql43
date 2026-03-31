class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        both = [[p, s] for p, s in zip(position, speed)]
        stack = []
        both.sort()

        for i in both[::-1]:
            print(i)
            distance, speed = i
            cur_time_till = (target - distance)/speed

            if len(stack) == 0:
                stack.append(cur_time_till)
            elif len(stack) > 0:
                car_infront_time = stack.pop()

                if cur_time_till <= car_infront_time:
                    stack.append(car_infront_time)
                elif cur_time_till > car_infront_time:
                    stack.append(car_infront_time)
                    stack.append(cur_time_till)

        return len(stack)
        