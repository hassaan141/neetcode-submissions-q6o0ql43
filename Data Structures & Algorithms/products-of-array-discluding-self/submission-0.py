class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ret = []
        out = {}
        total_product = 1
        total_product_no_zero = 0
        num_zero = 0

        for i in nums:
            if i == 0:
                num_zero += 1
                continue
            total_product *= i

        if num_zero > 1:
            return [0] * len(nums)

        if num_zero == 1:
            total_product_no_zero = total_product

        index = 0
        for i in nums:
            if num_zero == 0:
                out[index] = total_product // i
            else:
                if i == 0:
                    out[index] = total_product_no_zero
                else:
                    out[index] = 0
            index += 1

        ret = [out[i] for i in range(len(nums))]

        return ret
