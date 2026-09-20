class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # MENTAL MODEL 
        # for every string create an empty character counter 
        # map character counter: strings 
        # return list of strings with same characters counts which are therefore anagrams 
        
        seen = {} # hashmap to store character: counts 

        for st in strs: # for every string 
            count = [0] * 26 # initialize empty to counter to eventually store character counts 

            for c in st: # for every character in a specific string
                index = ord(c) - ord('a') # difference b/w ascii values gives exact index value 
                count[index] += 1 # update count at specific index value representing the character

            key = tuple(count) # keys have to remain hashable/immutable so change list to tuple 

            if key in seen: # if that character count exists in the hashmap already 
                seen[key].append(st) # add string to that list of strings 
            else: # otherwise 
                seen[key] = [st] # create key:value pair with an intialized list to add values to 
        
        return list(seen.values()) # return all list of values 

        # time complexity: 
        # O(m * n) - loop through n characters for up to m strings 
        # m = maximum number of strings 
        # n = max length of characters 
        # fast lookup and insertion for hashmaps is O(1)
        # so total time complexity is: O(m * n)


        # space complexity:
        # O(m) - storing information for up to m strings 
        # hashmap gets larger as the number of strings or input size gets larger 
        # so total space complexity: O(m)

