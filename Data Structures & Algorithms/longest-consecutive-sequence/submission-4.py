class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trying to figure out the longest consecutive sequence created from nums 
        # numbers don't have to be next to each other to be considered a sequence 
        # duplicates do not matter because they do no extend the sequence 

        seen = set(nums) # transform nums into a set for fast lookup
        longest = 0 # variable to track longest sequence in set 

        for num in seen: # for every value in seen 
            if num - 1 not in seen: # if there is not a value 1 number smaller than current element 
                current = num # variable to track where we are in the sequence (beginning)
                length = 1 # num is verfied to be the start of sequence and therefore an element in the sequence so length of sequence is considered 1 

                while current + 1 in seen: # if there is a value exactly 1 bigger than the current 
                    current += 1 # update current to track where we stand in the sequence now
                    length += 1 # add 1 to length because that element is also part of the sequence now 

                # now that we have the updated length 
                longest = max(longest, length) # compare max length of sequences so far to the length of current sequence and finally store the larger value 
        
        return longest # return the max length out of all consecutive sequences 