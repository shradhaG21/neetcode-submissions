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
      # The index represents the frequency.
      # Accessing freq[i] gives us the list of numbers that appear i times.
    
    
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

    # time complexity: 

    # hashmap is O(n) - becacause we have to look through the entire list of elements 
    # look ups inside are O(1) - so O(n) * O(1) = O(n)

    # frequency buckets - O(n + 1) because we have to create n + 1 buckets to be able access numbers at the maximum frequency which is the length of nums : ex: if an array has 6 elements the most amount of times that element can occur is 6, so we need to account for that, its also easier for indexing purposed 

    # for adding to the frequency buckets - worst case scenario we have n unique elements 
    # so we have to go through the entire hashmap n times 
    # appending is O(1)
    # so O(n) * O(1) = O(n)

    # finally the nested loop is NOT O(n^2) 
    # accessing buckets is still O(n + 1) 
    # now processing the buckets is also O(n) because every unique number stored in exactly one bucket, so across all buckets we are still accessing n elements 

    #"The inner loop isn't doing n work per bucket; it's doing n work total across all buckets."!!!
    # n numbers are spread across buckets - so total work is still O(n)
    # inner loop processes at most n numbers across all buckets 

    # final time complexity = O(n) + O(n) + O(n) + O(n)= O(4n) = O(n)

    # Space Complexity: 
    # count hashmaps: worst case scenario - O(n), worst case scenario every number only occurs once , so count has to store up to n entries 

    # nums = [1,2,3,4 ] - 4 diff hashmap entries as opposed to nums = [1,1,1,1] # one entr 

    # freq buckets: 
    # bucket structure grows with each n value - so we take up more memory 
    # n + 1 buckets so as the array increases so does the bucket structure 

    # res 
     #O(k) because res only stores the top k frequent elements , where k <= n 
     #because k can never be greater than the amount of numbers stored in numbs 
    
    # O(n) + O(n) + O(k) = O(n)

    # SPACE COMPLEXITY: O(n)

# count:
# Stores one entry for each unique number.
# In the worst case, every number is unique,
# so count can store up to n entries.
# -> O(n)


# freq:
# We create n + 1 buckets.
# The buckets grow based on the size of nums.
# Each unique number is also stored in one bucket.
# -> O(n)


# res:
# Stores k numbers.
# k can be at most n.
# -> O(k), which can be up to O(n)


# Overall:
# O(n) + O(n) + O(k)
# = O(n)

# what extra things did i create that will grow with n? always think about that !! - this will be count, freq, and res!!!! that is why we only considered those for time complexity!!!







