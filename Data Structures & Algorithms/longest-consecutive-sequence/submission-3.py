class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums) # seen is a set to easily check whether a number exists 
        longest = 0 # longest sequence is intially 0 because tracking has not started 

        for num in seen: # check every unique element in seen 
            if num - 1 not in seen: # verify if this is the first number in the sequence 
                current = num # if it is we are at the beggining of a sequence 
                length = 1 # already verified one element in the sequency so length = 1
                # start walking through element
                while current + 1 in seen: # while a conssecutive value exists 
                    current += 1 # updating current so next iteration can check for next element 
                    length += 1 # element is added to sequence so length is increased 

                longest = max(longest, length) # for every sequence, once length is updated find the longest length, so for example if length was 2 for one sequence, longest will be 2 , and then if we find another sequence with a length of 4, now longest = longest (2, 4) which will be 4
        
        return longest # finally return longest sequence length found so far 

        # Time complexity: 
        # seen = set(nums) - worst case every value is unqiue and seen stores n values - O(n)
        # for loop - processes n elements and runs for each element 
        # while loop does this not make this O(n^2) because it only runs if we have found the first element in a sequence and then only will it walk through the rest of the elements. The while loop will not run for an element that has an num - 1 value for it, so each element is being walked through only once and not being revisited. 
        # and lookup for example if num - 1 not in seen or while current + 1 in seen is O(1) because a hashset is being used 
        # so, total space complexity: O(n) + O(n) = O(2n) = O(n)

        # Space complexity: Think about data structures that are taking up space/memory
        # seen - used a set that worst case has to store n elements for n unique values and gets bigger as n gets bigger 
        # variables: longest, num, current, length - only store 1 value at a time - O(1)
        # total space complexity: O(n) + O(1) = O(n)

        