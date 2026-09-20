class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # MENTAL MODEL: use two frequency hashmaps to map characters:count 
        # loop through strings directly to store key:value pairs in hashamaps 
        # compare hashmaps to check if they are equal 

        seenS = {} # hashmap for string s 
        seenT = {} # hahsmap for string t 

        for st in s: # for every character in string s
            if st in seenS: # if the character already exists as a key in the hashmap 
                seenS[st] += 1 # add 1 to its current value 
            else: # otherwise 
                seenS[st] = 1 # create key:value pair and store count as 1 for first occurence 
        
        for st in t: # for every character in string t 
            if st in seenT: # if the character already exists as a key in the hashmap 
                seenT[st] += 1 # add 1 to its current value 
            else: #othrwise 
                seenT[st] = 1 # create key:value pair and store count as 1 for first occurence 

        # compare frequency maps to verify anagram 
        if seenS == seenT: 
            return True 
        return False 
        
        # Time Complexity: 
        # O(m + n) - worst case loop through all characters in string t and string s
        # m and n being the max length of characters per string 
        # hashmap lookup and insertion is O(1)
        # and since ther are 26 fixed keys comparing the hashmaps is also O(1)

        # Space Complexity: 
        # O(1) - worst case up to all 26 characters are stored in the hashmap 
        # since 26 is a constant and will not grow with input size n 

