class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use hashmap to map value: count 
        # create n + 1 empty buckets to make sure there is a bucket for every frequency 
        # populate buckets using data in hashmap 
        # access buckets at larger frequencies first 

        count = {} # hashmap to map elements: count 

        # use frequency map implementation to count frequency of elements 

        for num in nums: # for every element in nums 
            if num in count: # if elements already exists as a key
                count[num] += 1 # add 1 to current count 
            else: # otherwise 
                count[num] = 1 # first appearance of element so create key: value pair
        
        # create n + 1 empty buckets because maximum frequency for an element is the len(nums) and that index needs to be accessed 

        freq = [[] for i in range (len(nums) + 1)]
        # buckets created up to index n to represent max frequency of an element
        # [] - frequency 0 
        # [] - frequency 1 
        # [] - frequency 2 
        # [] - frequency n 

        # populate these buckets by grabbing data from hashmap 

        for n, c in count.items(): # for every key value in pair in hashmap 
            freq[c].append(n) # store elements with same frequency count in a list within a bucket in freq
        
        res = [] # array for storing final answer 

        # once buckets are populated access freq backwards so higher elements with high frequencies are accessed first 

        # start by accessing last index, excluding 0 - no element will have a frequency of 0 and decrementing by 1 to ensure we are going backwards
        for i in range (len(freq) - 1, 0, -1): 
            for n in freq[i]: # for every value in a specific bucket
                res.append(n) # store it in res 
                if (len(res) == k): # immediately check to see if length of array to k 
                    return res # if they are equal top k element have been found so we can return res 
