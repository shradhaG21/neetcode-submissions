class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
     # here we are using a hasmap to map the value:index 
     # we are also looking for the complement 
     # complement = target - n
     
        seen = {}

        for i, n in enumerate (nums): # loop through both index and value 
            complement = target - n
            if complement in seen: # if our complement is in the hashmap 
                return [seen[complement], i] #return index value mapped to complement, index of n
            seen[n] = i #otherwise we will map current value to the index and store to keep track until our complement is found 
        return 

# Time complexity: O(n) because we are using a for loop and hashing O(n) * O(1) = O(n) - hashing happens inside for loop so we are multiplying O(1) * n iterations 
# Space complexity: O(n) because worst case scenario we go through every element in nums so our hashmap stores every n value and gets bigger taking up more memory 
    