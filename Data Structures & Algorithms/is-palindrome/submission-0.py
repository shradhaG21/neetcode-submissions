class Solution:
    def isPalindrome(self, s: str) -> bool:
        # MENTAL MODEL: 
        # skip junk like spaces and punctuation
        # compare real characters 
        # if they match, move inward. 
        # if no mismatches occur within the string, the string is a valid palindrome. 

        # initalize to pointers representing opposite ends of the string
        left = 0 # beginning
        right = len(s) - 1 # end 

        while left < right: # while there are still more characters left to compare 
                # skip characters in the beginning if they are junk (spaces and punctuation)
                # still have to make sure left < right because this check might skip multiple characters 
                # python does not automatically jump back up and redo the check for the new pointer position
                while (left < right and not s[left].isalnum()): 
                    left += 1
               
                while (left < right and not s[right].isalnum()): # same logic applied here 
                    right -= 1
                
                # by now, we have reached real characters (numbers or letters) and can compare them
                if (s[left].lower() != s[right].lower()): # case sensitivity does not matter here 
                    return False # if the characters are not equal, return False 

                # if they are eqal move inward, to compare next set of characters 
                left += 1
                right -= 1

        return True # if we go through the entire string without ever finding a mismatch, the string is a valid palindrome, so we can return True 

        # Time Complexity: 
        # even though there are nested while loops, the time complexity is not O(n^2)
        # this is because each pointer (left and right) only visit each character maximum once 
        # they also only move in one direction 
        # so, if n = max length of characters: 
        # they loop through a string n times, visiting each character once
        # O()
                