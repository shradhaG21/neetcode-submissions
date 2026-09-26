class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # sort array to apply two pointers intelligently, smallest to greatest value placement

        res = [] # array to store final answers 

        for i in range (len(nums)): # locks down first number in the triplet 
            if i > 0 and nums[i - 1] == nums[i]: # we want unique triples, this helps avoid duplicates in the beginning
                continue 
            
            left = i + 1 # start left pointer after i so we are not rechecking/revisiting same combinations 
            right = len(nums) - 1 # right pointer starts at very last index because that is the max value 

            while left < right: # while the two pointers are no equal/have not crossed paths 
                total = nums[i] + nums[left] + nums[right] # target sum of 0 
                
                if total < 0: # if total is negative then the move the left pointer towards larger values 
                    left += 1
                elif total > 0: # if total is positive then move the right pointers towards smaller values 
                    right -= 1
                else: # total is 0, so a valid triplet has been found
                    res.append([nums[i], nums[left], nums[right]])

                    # update values of left and right pointers 
                    left += 1
                    right -= 1

                    # while left is still less than the right pointer, check to see if other valid triplets can be found for the same i 
                    while left < right and nums[left] == nums[left - 1]: # check to see that for duplicatese, because positions were updated  
                        left += 1 # skip any duplicate values 

        return res # return all valid triplets 