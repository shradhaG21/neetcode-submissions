class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # MENTAL MODEL: has this value already been visited/stores 
        # fast loopup/ existence - hashset 

        seen = set() # set to keep track of values visited in nums 

        for num in nums: # for every value in nums call current value 
            if num in seen: # if value already in seen - means already visited 
                return True # return true 
            else: # otherwise first occurence of value 
                seen.add(num) # store it in set to reference values visited 
        
        return False # return False if not duplicate exists 

        # Time complexity: 
        # worst case - scan entire array before duplicate is found or no duplicate is found - O(n)
        # set lookup and insertion O(1)
        # total time complexity: O(n) * O(1) = O(n)

        # Space Complexity: 
        # what data structure was created? hashset 
        # worst case - set has to store all n unqiue elements if no duplicate exists 
