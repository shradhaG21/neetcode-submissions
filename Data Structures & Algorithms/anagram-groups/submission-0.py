class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} #sorted string as group label: all related strings 

        for st in strs: #for every current string in the array 
            s = "".join(sorted(st)) #sort the current string so we have the group label 

            if s in seen: # if the sorted string is in seen that means group has been created already
                seen[s].append(st) #so we can append the string to the list 
            else: #otherwise 
                seen[s] = [st] #we have to create the new group and create a list 
        
        return list(seen.values()) #return the list of all values in the hashmap 
        
       
    