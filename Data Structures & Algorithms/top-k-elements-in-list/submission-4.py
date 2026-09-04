import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return []

        freqMap = {}
        numList = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for key,val in freqMap.items():
            numList[val].append(key)
        
        result = []

        for n in range(len(numList) - 1, -1, -1):
            for i in numList[n]:
                result.append(i)
                if len(result) == k: return result

        return result