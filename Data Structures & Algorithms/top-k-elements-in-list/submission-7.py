class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # MENTAL MODEL: 
        # use hashmap to map values:count 
        # create n + 1 buckets - max frequency of a number is length of nums - (BUCKET SORT!!)
        # populate buckets by grabbing data from hashmap 
        # traverse backwards to grab elements with higher frequencies first 

        seen = {} #hashmap to map value: count 

        # use a frequency map to correctly map value:count 
        for num in nums: 
            if num in seen: 
                seen[num] += 1
            else: 
                seen[num] = 1 
        
        # create n + 1 buckets to store values at specific frequencies (index = frequency)
        freq = [[] for i in range (len(nums) + 1)]
        # freq = [
        # [] - frequency 0 
        # [] - frequency 1
        # [] - frequency 2 
        #]

        # grab items from hashmap to populate the buckets 
        for n, c in seen.items(): # for every key:value pair in the hashmap 
            freq[c].append(n) # for every frequency/count value store an n value 

        # freq = [
        # [] - frequency 0 
        # [3] - frequency 1
        # [5, 8] - frequency 2 
        #]

        res = [] # initialize array to store final answers
        
        # traverse through freq backwards to grab numbers with higher frequencies first 
        # starting at the very last index, decrementing by 1, and excluding 0 because no element will have a frequency of 0 
        for i in range (len(nums), 0, -1): 
            for n in freq[i]: # for every frequency grab all n value in that specific bucket 
                res.append(n) # store it in res 
                if (len(res) == k): # immediately check to see if length of res and k are equal 
                    return res 


