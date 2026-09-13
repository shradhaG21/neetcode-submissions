class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       # MENTAL MODEL: sorted string: anagrams 

        seen = {} # empty hashmap to store key-value pairs 

        for st in strs: # for every string in strs 
            s = sorted(st) # s will be the key - but this gives list - not hashable 
            s = "".join(s) # so ["a", "e", "t"] becomes "aet" - now hashable - bc strings are immutable
            if s in seen: # if sorted string exists as key in seen
                seen[s].append(st) # append to the already existing list 
            else: # otherwise 
                seen[s] = [st] # create a key: value pair with list as values 
        
        return list(seen.values()) #return all values in seen in list form 

       # ex: Input: strs = ["act","pots","tops","cat","stop","hat"]
       # n = 6 - number of strings 
       # k = maximum length of string - remember worst case 
       # NOW LOOK AT THIS CODE SPECIFICALLY 
       # for st in strs: # for n iterations ["eat", "cat", "tea"] - 3 iterations
       #  s = sorted(st) # we are sorting k characters - 3 characters sorted for each string 
       #"eat" → sort k characters → O(k log k)
       #"tea" → sort k characters → O(k log k)
        #"tan" → sort k characters → O(k log k)
# because its inside a for loop you do O(n * klogk)
# the hashmap operations are O(1) - so they don't dominate the sorting 


# Space complexity - think about what data structure we created 
# hashmap - hashmap has to store information for n strings 
# for each string - there are also k characters
# as n increases we have store more strings/info 
# as k increase our sorted strings/keys as well as our grouped strings get larger 
# we multiply it because worst case - we have n strings each with k characters 
# so space complexity = O(n*k)















        
    
