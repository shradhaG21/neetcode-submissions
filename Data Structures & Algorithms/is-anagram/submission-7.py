class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #MENTAL MODEL: 2 hashmaps - one for each string - map characters: count 
        # compare hashmaps - if equal - return 
        # use frequency maps 

        seenS = {} # hashmap for string s to map characters: count
        seenT = {} # hashmap for string t to map characters : count 

        for st in s: # can loop through string directly in python
            if st in seenS: # if character exists as key in hashmap 
                seenS[st] += 1 # add 1 to current character count
            else: # otherwise - first occurence 
                seenS[st] = 1 # create key:count pair in hashmap 
        
        for st in t: # can loop through string directly in python 
            if st in seenT: # if character exists as key in hashmap 
                seenT[st] += 1 # add 1 to current character count
            else: # otherwise - first occurence 
                seenT[st] = 1 # create key: count pair in hashmap 
        
        if seenS == seenT: # check to see if hashmaps are eqaul 
            return True 
        return False 


        