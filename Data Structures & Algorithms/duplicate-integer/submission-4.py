class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     
     seen = set() #start of with an empty set - we are using a set because only care about the existence of the number 

     for num in nums: # loop through every number in the array 
        if num in seen: #if it has beeen seen before
          return True # return true because it means that we found a duplicate
        seen.add(num) #otherwise - else is not needed here because the return statement ends function and we will add the num to the set otherwise to keep track of every number we have visited 
     return False

    