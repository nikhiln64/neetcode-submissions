class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countOfZeros = 0
        for n in nums:
            if n == 0:
                countOfZeros += 1
            else:
                product *= n
        
        if countOfZeros > 1:
            return [0] * len(nums)


        # res = [0] * len(nums)
        for i in range(len(nums)):
            if countOfZeros > 0:
                nums[i] = product if nums[i] == 0 else 0
            else:
                nums[i] = product // nums[i]

        return nums

