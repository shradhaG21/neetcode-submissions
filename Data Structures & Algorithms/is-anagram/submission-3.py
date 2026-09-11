class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
   
    # we are going to implement frequency maps here and the character will be our key and the count or frequency of it will be our value 

    # since we are looping through different strings we will have 2 different hashmaps and then we will compare them to check if they are equal and if they are that means we have a valid anagram 

        seenS = {} # start of with an empty hashmap for string S
        seenT = {} # start of with an empty hashmap for string T 

#remember we can loop through strings directly instead of needing an array because a string is already an array of characters
        for st in s: # for every character in string s
            if st in seenS: #if that character already exists in the hashamp
                seenS[st] += 1 #add 1 to the count
            else: 
                seenS[st] = 1 #other it is the first appearance so we are going to store the value as one 
    
        for st in t: #for every character in string t
            if st in seenT: #if character already exists in the hashmap 
                seenT[st] += 1 #add 1 to its current count
            else: #if not 
                seenT[st] = 1 #it is probably its first appearance so store the current count as 1
    
        if seenS == seenT: #if hashmaps are equal that means the 2 strings are valid anagrams 
            return True # return true if they are 
    
        return False # otherwise return false 



    #Time Complexity = O(n) - because we are using for loops and hashing - but we take the slower algorithm 

    #Space Complexity = O(n) - because we have to store each character and the count in the hashmap. 