class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # MENTAL MODEL: 
        # use frequency map to count frequency of all elements 
        # create empty n + 1 buckets to store elements where index = frequency 
        # pull data from hashmap to populate buckets 
        # traverse backwards to acquire higher frequencies 
        # once len(result array) = k, return list 

        count = {} # hashmap to count frequency of elements 
        
        # create frequency map to map element: count 
        for num in nums: 
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1 

        # create n + 1 buckets to store elements at specific frequency indexes 
        # create n + 1 buckets to access last index (maximum frequency of element is len(nums))
        freq  = [[] for i in range (len(nums) + 1)] # stores a list of lists 
        # [] frequency 0
        # [] frequency 1
        # [] frequency 2

        # get data from hashmap to populate those buckets so elements can be stored 
        for n, c in count.items():# hashmap maps n:c - element to count
            freq[c].append(n) #store element in freq at specific index to accurately represent frequency
        # ex: 
        #[]
        #[5.8] -  elements that have a frequency of 1 in nums
        #[2] - elements that have a frequency of 2 in nums 

        res = [] # array to store final answer 
        
        # once populated scan freq backwards to grab elements with higher frequency first 
        # include last index - maximum frequency of an element is the length of the array 
        # exclude 0 - no element will have a frequency of 0 
        # decrement by 1 - working backwards 
        for i in range (len(nums), 0, -1): 
            for n in freq[i]: # for every element in the bucket 
                res.append(n) # add element to res 
                if (len(res) == k): # immediately check to see if top k elements have been found
                    return res # return array with top k frequent elements 
        
        

