class Solution:

    # MENTAL MODEL 
    # store strings with length and # in front of string for the encode function
    # store it this way so decode knows the exact amount of characters to grab per string 
    # create two pointers for the decode - one to mark the starting point of a string and then one that will actually move through the string 

    def encode(self, strs: List[str]) -> str:
        res = [] # array to store final string 
        
        for s in strs: # for every element in strs
            res.append(str(len(s)) + "#" + s) # currently ["4", "#", "neet"]

        return "".join(res) # now stores as "4#neet"

    def decode(self, s: str) -> List[str]:
        res = [] # array to store final answer with separated strings 
        i = 0 # intialize first pointer to mark the beginning of string 

            # intilalize second pointer - this will move through the string 
            # they will start at the same point but i will mark the beginning of the string and j will help us find the length and exactly how many characters to grab per string
        while ( i < len(s)): # while there is more to decode 
            j = i
            
            while (s[j] != "#"): # keep moving j until "#" - everything before that is the length - needed to turn get character at j not j itself 
                j += 1
            
            length = int(s[i:j]) # length will be everything between i and j - excluding j - change length back to int becuase otherwise we would be trying to grab a string index value - causes errots 

            res.append(s[j + 1: j + length + 1]) # right after j is when the string begins and after that we have to grab exactly length characters to get to the end of the string. 

            i = j + length + 1 # this is the beginning of the next string for the next iteration 
        
        return res # finally return res 


