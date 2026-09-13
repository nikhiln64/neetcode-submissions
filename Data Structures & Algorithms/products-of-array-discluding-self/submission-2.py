class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfPrefix(nums)
        product = 1
        countOfZeros = 0
        for n in nums:
            if n == 0:
                countOfZeros += 1
            else:
                product *= n
        
        if countOfZeros > 1:
            return [0] * len(nums)


        for i in range(len(nums)):
            if countOfZeros > 0:
                nums[i] = product if nums[i] == 0 else 0
            else:
                nums[i] = product // nums[i]

        return nums
    """


