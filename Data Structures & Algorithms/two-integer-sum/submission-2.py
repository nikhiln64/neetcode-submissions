class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in hashMap:
                return [hashMap[sum], i]
            hashMap[nums[i]] = i

        return []
                