class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # MENTAL MODEL: map value: index 
        # loop through and grab both index and current value 
        # store values to eventually figure out the complement of a number 
        # complement = target - n, n being the current number 

        seen = {} # hashmap to map value: index

        for i, n in enumerate (nums): # enumerate function grabs index, value 
            complement = target - n # complement = total sum - current value
            if complement in seen: # if complement exists as a key in seen 
                return [seen[complement], i] #return the index of complement, current index 
            seen[n] = i # store current value:index pair 
        
        # also complement is the smaller index because that value is stored at an earlier iteration in comparison to current index value because to find complement of a value the complement must be stored first in seen. 

        # Time complexity: 
        # O(n) - worst case we have to loop through all of nums before a complement is found and store all values in hashmap or a complement might not exist at all. Loop through values in nums is O(n) and lookup and insertion in hashmap is O(1). 
        # so, total time complexity: O(n) * O(1) = O(n)

        # Space Complexity: 
        # Think about what data structures we have created? Created a hashmap which has to store up to n elements if no complement exists in nums. It also gets bigger as the input size gets bigger - O(n)

