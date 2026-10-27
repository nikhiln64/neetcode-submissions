class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            countMap[i] = countMap.get(i, 0) + 1
        
        for key, val in countMap.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return []
