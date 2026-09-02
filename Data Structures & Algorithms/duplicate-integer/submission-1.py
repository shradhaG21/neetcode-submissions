class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     
      seen = set() #O(1)
      for num in nums: #O(n)
       if num in seen: #O(1) - uses hasing
        return True
       else:
        seen.add(num) #O(1)


      return False


      # Time complexity - O(1) + O(n) * O(1) + O(1) = O(n)


      # 1.) Start with an empty set that we can add values of num to
      # 2.) loop through every value in num
      # 3.) If num is in the hasmap already - we will return true
      # 4.) Otherwise we will add it to the hashmap
      # 5.) After looping 1, 2, 3  are added but once it sees 3 it returns true
      # 6.) We get the confirmation that 3 was the repeated value.
     
