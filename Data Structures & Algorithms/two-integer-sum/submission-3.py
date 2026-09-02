class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
     Answer = []

     for i in range (0, len(nums)): 
        for x in range (i + 1, len(nums)): 
            if (nums[i] + nums[x] == target): 
                Answer.append(i)
                Answer.append(x)
     
     return Answer 
   


 


