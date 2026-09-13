class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hashmap - map sorted string: strings with same characters 
      
      seen = {}

      for st in strs: # for every string in strs
            s = sorted(st) # s is the sorted string/key - this gives a list and we cant use that as our key 
            s = "".join(s) # so we must join it into a string
            if s in seen:  # now if the string is in seen 
                seen[s].append(st) # access the list stored at key s and add the current string st to that list
            else: 
                seen[s] = [st] #other we will store the first strinf if seen is empty 
            # this will also be a list because remember our values will be a list 
    
      return list(seen.values()) #return all the grouped anagrams that exist in our hashmap 


# Time Complexity = O(n * k log k)
# n = the NUMBER of strings in strs, and k = the LENGTH of each string.
# This is different from Valid Anagram, where n and m represented the lengths
# of the two individual strings.
# Here we have n different strings, so we loop through all n strings.
# For each string, we sort its k characters, which takes O(k log k).
# Since sorting happens for every string, we multiply:
# O(n) * O(k log k) = O(n * k log k).


# Space Complexity = O(n * k)
# n = the NUMBER of strings and k = the LENGTH of each string.
# Space complexity measures how much extra memory the algorithm needs.
# We store information for the strings in our hashmap.
# The length of a string matters for memory because a longer string contains
# more characters, and therefore requires more memory to store.
# So we account for both the number of strings (n) and their length (k):
# n strings * k characters = O(n * k) space.


# IMPORTANT:
# In Valid Anagram, n and m ARE the lengths of the two strings, so string
# length was already being considered in O(n + m).
# In Group Anagrams, n represents the NUMBER of strings, so we need another
# variable k to represent the LENGTH of those strings.
    
