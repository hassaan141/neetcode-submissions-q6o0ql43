import heapq as heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [i[1] for i in min_heap]           

        