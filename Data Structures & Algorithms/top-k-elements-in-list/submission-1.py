class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

       count = {} #hashmap to store values:count 

      # create a frequency map for every n:count 
       for n in nums: 
            if n in count: 
                count[n] += 1
            else: 
                count[n] = 1 
       # create a freq list with empty buckets
       # go up to len(nums) + 1 bc an element can occur up to the length of nusm 
       # [1,1,1,1,1,1] at freq[6] we want to store 1 - need to account for that edge case
       # frequency is also the index  
       # by accessing freq at a specific index - we get the value mapped to a specific freq 
    
    
       freq = [[] for i in range (0, len(nums) + 1)] #creates empty buckets up to n + 1

       # before: 
       # freq [
       # []
       # [] 
       # [] 
       # []
       # []
       # []
       # []]
      

       for n,c in count.items(): # takes items from hashmaps and fills buckets 
            freq[c].append(n) # every frequency bucket now stores an n value 
       # after:                                      ^
       # freq [                                      |
       # []                                          |
       # [1] # 1 stored in bucket with index 1       | Traverse through list 
       # [5,8] # 2 stored in bucket with index 2       | backawars so we access 
       # [3] # 3 stored in bucket with index 3       | higher frequencies first. 
       # []                                          |
       # []                                          |
       # []]                                         |

       res = [] # this where final answer is stored
# traverse through freq backawards, from last index excluding 0 bc no element will have freq of 0 and decrementing by 1. 
       for i in range (len(freq) - 1, 0, -1): # accessing a specific index value in freq 
         for n in freq[i]: # freq[2] = [5,8] go through that list and for every value in that list
            res.append(n) #add it to res 
        
            if len(res) == k: #once the length of res == k, we have accessed top k frew elements
                return res # so we can return res 

