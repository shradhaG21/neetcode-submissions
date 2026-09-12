class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} #frequency map for mapping value:counts 

        for n in nums: # for every value in nums call current value
            if n in count: #if the value already exists
                count[n] += 1 #add 1 to current count
            else: #otherwise 
                count[n] = 1 #first appearance so count = 1
    
    #now create empty buckest so that the frequency = index, essentially 
    # freq[3] = 1, a specific frequency index stores the numbers that appear that many times

    # creating empty buckets - going up to last index bc a number can appear up to len(nums)
        freq = [[] for i in range(len(nums) + 1)] #for every empty bucket essentially

        for n, c in count.items(): # n = number/value and c = count (getting all the vals from hashmap )
            freq[c].append(n) #so for every count we are mapping an n 
    
        res = [] #this is where we still our result 

#go from last index excluding 0, cause every element will appear once and decrement by 1 
        for i in range (len(freq) - 1, 0, -1): 
            for n in freq[i]: #this is saying for every n value in frequency 
                res.append(n) #add that specific value to res 
    
                if (len(res) == k): #makes sure all k elements are counted properly 
                    return res 



