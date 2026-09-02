class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
     # Fast lookup 
        Answer = [] # Empty list 
        
        for x in range (0, len(nums)): #for every index starting at 0 in nums 
            for y in range (x + 1, len(nums)): #for every index starting after x because we have to make sure they are not the same, so it y would start at the next index 
                if ((nums[x] + nums[y]) == target): #if the values add up to the target value and the indexes are not the same 
                    Answer.append(x) #we will add the index value to the list 
                    Answer.append(y) # we will add the second index value to the list 
        
        return Answer #finally we will return the list 

     






