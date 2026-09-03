class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     
     # Using a set because a set cares about whether or not an element exists 
      seen = set()
      for num in nums: # for every element in the array 
        if num in seen: #handle edge case first and return true if element has been already
          return True 
        seen.add(num) #otherwise add the element to the set to track the elements we have visited 
      
      return False #if all of this is false, return false 