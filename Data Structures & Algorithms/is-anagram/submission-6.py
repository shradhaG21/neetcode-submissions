class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
   
        # MENTAL MODEL: create two freq maps and compare them at the end 
        # mapping character: frequency 
        seenS = {} # map for string s
        seenT = {} # map for string T 

        # in python you can loop through strings directly 
        for st in s: # for every character in string s
            if st in seenS: # if the characters exists as key in seenS
                seenS[st] += 1 # add 1 to current frequency 
            else: # otherwise 
                seenS[st] = 1 # first appearance, frequency = 1 
        
        for st in t: # for every character in string t
            if st in seenT: # if the character exists as a key in seenT
                seenT[st] += 1 # add 1 to current frequency
            else: # otherwise 
                seenT[st] = 1 # first appearance, so frequency = 1
        
        #compare both hashmap 
        if seenS == seenT: # if both are valid anagrams 
            return True # return True 
        return False # return False 


        # Time Complexity: 
        # both hashmaps - O(1)
        # for n iterations * hashing - O(n) * O(1)
        # or O(m) * O(1) = O(m)
        # n and m being the length of respective strings 
        # total time complexity = O(n + m) = O(n)

        # Space Complexity: 
        # created two hashmaps 
        # worst case scenario - each have m or n unqiue characters 
        # both get bigger as the length of strings get bigger 
        # total space complexity = O(n + m) = O(n)