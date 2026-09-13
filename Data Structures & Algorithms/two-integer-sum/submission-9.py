class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # mapping value: index 
     # complement = target - s

        seen = {} # empty hashmap useful for finding complement 
        
        for i, n in enumerate(nums): # tracking both current number and index 
            complement = target - n # complement is what we are looking for 
            if complement in seen: # if the complement exists in hashmap 
                return [seen[complement], i] #complement's index, current index
            seen[n] = i # otherwise we can store current n:i pair 
        
        # time complexity: 
        # for n interations * hashing = O(n) * O(1) = O(n)
        # worst case scenatio - scan through n elements before a complement is found 

        # space complexity: 
        # what new data structures have we created: seen 
        # hashmap - gets bigger as n gets bigger 
        # worst case scenario - hashmap stores n elements before a complement is found 
        # total space complexity - O(n)



     