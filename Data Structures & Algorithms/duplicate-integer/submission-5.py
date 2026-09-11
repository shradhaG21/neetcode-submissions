class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     
        # remember a set only cares about whether a value exists or not 

        seen = set() #this is how you define a set as opposed to a hashmap which is a dictionary 
     
        for num in nums: #for every number in nums call the current value 
            if num in seen: #if num exists in the hash set - remember starting out the set is empty 
                return True #return true if value has already been seen - keeping track of value
            else: 
                seen.add(num) #otherwise add the current value to the set to keep track of what we have already seen 
        return False 

        # Time complexity : O(n) + O(1) = O(n) this is because we are hashing and then also we have a for loop so we take the slower time complexity 

        # Space complexity : O(n) because worst case scenario we loop through every element in nums so we have to keep adding values to our set meaning we have to remember more values which means we are taking up more space!
    
    