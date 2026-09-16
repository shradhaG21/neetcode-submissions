class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        res = [1] * len(nums) #place holder array 
        prefix = 1 # running product of elements to the left of current elemnt 

        for i in range (len(nums)): 
            res[i] = prefix # in res store product of previous elements excluding current elemnt 
            prefix *= nums[i] #multiply current element into prefix product for next iteration so res can stor it correctly 
        
        postfix = 1 # running product of all elements to the right of current elemetn
        
        # go backwards so that as we reach current elements, we can keep track of products already calculated to the right 
        for i in range (len(nums) - 1, -1, -1): # starting at last index to first index, backwards by 1
            res[i] *= postfix #multiply left side products by right side products and store answer
            postfix *= nums[i] #multiply the current value by the postfix product so that it is updated for the next iteration 
        
        return res # return products of array except self 

    
    # Time complexity: O(n)
    # this is because we have 2 loops both processing n elements - so that id O(n) + O(n) = O(2n) = O(n)

    # Space complexity: think about variables and data structures created 
    # posfix/prefix - variables that store one value at a time - O(1)
    # res [] - data structure that hold final answer and will store n elements for an input array of n elements and if the input array has more elements so will res, meaning it will take up more memory. 