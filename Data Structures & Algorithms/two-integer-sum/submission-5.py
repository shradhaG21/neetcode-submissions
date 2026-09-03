class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
        #Using a hashmap to map [value:index]
        #keep track of complement 
        # target - current = complement 
        # dictionary[key] = value
        seen = {}

        for i, n in enumerate(nums): #keep track of both the index as well as current 
            complement = target - n # calculate what our complement is 
            if complement in seen: # if it is already in the map
                return [seen[complement], i] # return the value/ index of complement, current index 
            seen[n] = i #othewise store the index value of our current element 
        return 