class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
        prevMap = {} #initialize an empty hashmap to store every value we have visited 

        for i, n in enumerate(nums): #We need to keep track of the current number as well as the index 
            diff = target - n # our difference is the complement which is our target value - current value 
            if diff in prevMap: 
                return [prevMap[diff], i] #return index of diff and the index of current value 
            prevMap[n] = i #otherwise just store the current value and its index
  
        return

# Explanation/ Mental 

# prevMap = {}
# ↓
# "Remember numbers I've seen and their indexes."


# Look at a number.
# ↓
# "What other number do I need to reach target?"
# ↓
# diff = target - current number
# ↓
# "Have I already seen that number?"
#         ↓
#      YES → return its index + my current index
#         ↓
#       NO → remember current number + current index







 


