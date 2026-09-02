class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            sumVal = target - nums[i]

            if sumVal in hashMap:
                return [hashMap.get(sumVal), i]
            hashMap[nums[i]] = i

        return []
        