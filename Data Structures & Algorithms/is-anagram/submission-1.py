class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        seenS = {} # Two empty maps that we are going to add key - value pairs to and    compare them at the end
        seenT = {} # Same idea here
       
       #Use frequency maps and compare at end to compare occurence of specific characters
       #  s = [] - dont have to do this because python can loop through strings directly and it treats strings as a sequence of character for looping purposes
       #  t = []

        for st in s: # for every character in the string
            if st not in seenS: #if the character is not in the map
                seenS[st] = 1 # since it is the first occurence of the character the value will be 1
            else:
                seenS[st] += 1 # otherwise we will add 1 to the current value
       
        for st in t: #for every character in t
            if st not in seenT: # if that character does not exist in the map
                seenT[st] = 1 # since its the first occurence the value will be one
            else:
                seenT[st] += 1 #otherwise we will add 1 to the current value
       
        if seenS == seenT: # in the end we will compare the hashmaps
            return True # if they are equal we will return true and the two strings are valid anagrams
       
        return False