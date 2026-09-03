class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
    # we are using a hashmap because we are trying to store the character itself as well as how frequently they occur {element:frequency}

    #We will using two frequency maps and then comparing them at the end to see if they are qual 


        seenS = {}
        seenT = {}

        for st in s: 
            if st in seenS: 
                seenS[st] += 1
            else: 
                seenS[st] = 1
    
        for st in t: 
            if st in seenT: 
                seenT[st] += 1
            else:
                seenT[st] = 1
        
        if seenS == seenT: 
            return True 
    
        return False 
