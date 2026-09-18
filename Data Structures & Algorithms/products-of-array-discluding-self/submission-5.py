class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # MENTAL  MODEL: 
        # scan elements left of current element and calculate prefix product 
        # scan elements right of current elmement and calculate postfix product 
        # multiply prefix and postfix product to get products of array except self 

        res = [1] * len(nums) # create place holder initially storing prefix product 
        prefix = 1 # prefix is initialized to 1 because nothing exists to the left of first element 

        for i in range(0, len(nums)): 
            res[i] = prefix # store product of elements to the left of current element 
            prefix *= nums[i] # multiply prefix product by current element to update prefix product for next iteration before it is stored 
        
        postfix = 1 # postfix is initialized to 1 because nothing exists to the right of last product in the array 

        # remember rest current stores left side products 
        # so by multiply postfix value into it we are storing the final answer at a specific index
        # start scanning from right to left, starting at last index to first index 
        for i in range (len(nums) - 1, -1 , -1):
            res[i] *= postfix #store final answer in res by multiplying prefix product and postfix 
            postfix *= nums[i] # include current element so that for next iteration we have the correctly calculated right side product so that when we go to multiply it by prefix product the final answer is stored correcly. 
        
        return res # return final answer 
