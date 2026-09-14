class Solution:

    #MENTAL MODEL: store strings with length and # 
    # are able to understand start and end of the strinf 
    # know exactly how many characters to grab

    # most efficient code for encode function 
    # strings are immutable so if res += used 
    # create new strings and copy old contents over and over
    def encode(self, strs: List[str]) -> str:

        res  = [] # empty list to store final string eventually sent to decode 

        for s in strs: # remember we have to typecast len(s) to a string 
            res.append(str(len(s)) + "#" + s) # append each word to list ex: ["4#neet", "3#you"]
        
        return "".join(res) # join the list into one concatenated string - 4#neet3#you - decode recieves this  


    def decode(self, s: str) -> List[str]:

        res = [] #empty list to store final contents 

        i = 0 #create intial pointer to start at the beginning of string 

        while (i < len(s)): #keep decoding encoded string until end of string is reached 
            j = i # create second pointer that will be incremented so we length can be found 

            while (s[j] != "#"): #keep incrementing until # is found because before that is the length 
                j += 1
        
            length = int(s[i:j]) # change length back into an int and in between i and j = length 

            res.append(s[j + 1: j + 1 + length]) #start right after j because that where the string starts 
        # and move length characters away from j to ensure entire string was captured 

            i = j + 1 + length # this sets the pointer to the start of the next encoded string and the entire process repeats 
        
        return res # finally return the decoded list 
    

    # Encode: 
    # time complexity: O(m) - m is the total list of characters that are being processed 
    # ENCODE TIME: O(m)
# m = total number of characters across all strings
#
# Even though we don't explicitly loop through each character,
# creating the encoded strings requires copying the characters
# from each original string. we have to copy characters from each string 
#
# Across all strings, we copy/process m total characters.
# Therefore: O(m)
    # space complexity: O (m + n) - m characters are being stored but also n number of strings 
    # remember for space complexity we have to ask ourself what data structure was created - we created res [] and when we appended to it was n strings with m characters 

    # Decode: 
    # time complexity: O(m) - again processing a list of m characters 
    # space complexity: O(m + n) - storing m characters but also n strings within the list 
    # same here created res[] to store n strings with m characters 


