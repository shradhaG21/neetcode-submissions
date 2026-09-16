class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)  # create one slot for each index
        prefix = 1  # running product of everything to the left

        for i in range(len(nums)):
            res[i] = prefix  # store the prefix product for this index
            prefix *= nums[i]  # include current value for the next iteration

        postfix = 1  # running product of everything to the right

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # combine left product with right product
            postfix *= nums[i]  # include current value for the next index to the left

        return res