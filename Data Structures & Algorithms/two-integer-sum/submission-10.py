class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # MENTAL MODEL: hashmap : map value and index 
        # keep track of complement 

        seen = {} #hashmap to to map value: index 

        for i, n in enumerate(nums): #enumerate grabs index and value at the same 
            complement = target - n # complement is total sum - current number 
            if complement in seen: # if complement exists as a key in seen
                return [seen[complement], i] # return index of complement and current value's index
            seen[n] = i # otherwise store current value:index pair if current number is a complement for a different number 
        return 
        