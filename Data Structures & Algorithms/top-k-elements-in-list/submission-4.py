class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      count = {} #hashmap to map numbers:count 
      
      # creating the frequency map 
      for num in nums: # for every value in nums call current num
        if num in count: # if num exists in count
            count[num] += 1 # add one to current frequency 
        else: # otherwise its the first appearance 
            count[num] = 1 # so current frequency is 1 
      
      # implement bucket sort - create a list of n + 1 buckets 
      # n + 1 buckets because the maximum amount of time a number 
      # can appear is n times so we need to be able to access 
      # that frequency, therfore we need an index value for that bucket 
      freq = [[] for i in range (len(nums)+ 1)]
      # create a bunch of empty buckets - place holders to store actual values
      # freq = [
      # [] - frequency 0 
      # [] - frequency 1 
      # [] - frequency 2 
      # ...] 

      # populate these buckets using info from count 
     
      # have to do n,c because in our hashmap we mapped number to frequency 
      for n, c in count.items(): # for every count/index - add a list of value/values 
        freq[c].append(n) # remember frequency is a list of lists 
      
      # after populating, loop through freq backwards 
      # so we can access higher freq first and append them.

      # we need another list to store final result 
      res = []
     
      # starting by accessing the very last index - bc that's the highest frequency 
      # excluding 0 bc no elements will have a frequency of 0 
      # decrementing by 1 to ensure we are traversing backwards
      # remember freq is a list of lists [5,8] - so multiple numbers can exist for a specific frequency 
      # second for loop to make sure we are appending every number from that list into res 
      # if that list contains multiple numbers 
      for i in range (len(freq) - 1, 0, -1):
        for n in freq[i]: 
            res.append(n)

            if len(res) == k: # if the len of res matches k, top k elements have been found
                return res # return res 
      

      # time complexity: 
      # hashmap - n iterations * hashing = O(n) * O(1) = O(n)
      

      # empty buckets - created n + 1 buckets because maximum amount of times a value can appear is n times and we need to be able to access that index/frequency = O(n + 1) = O(n)

      # populating the buckets: going through all n numbers in the hashmap and appending them to freq 
      # n iteration * O(1) = O(n)

      # nested loop - O(n)
      # this is because the outer loop is going through the buckets which is n iterations 
      # the inner loop is processing everything stored across all buckets 
      # so its still n iterations across all buckets because every number is uniquely stored in a bucket 
      
      # total time complexity : O(n) + O(n) + O(n) + O(n) = O(4n) = O(n)

      # space compexity: 
      # think about all the new data structures we created 

      # hashmap - gets bigger and has to store more info as n gets larger 
      # worst case - n unique elements - so have to store key : value pairs for each elements 
      # so it keeps bigger 

      # freq - O(n + 1) = O(n) because we created n + 1 buckets to be able to access the last index and 
      # doing freq[c-1].append(n) is a lot messier 
      
      # res - O(k) - this is because res will only hold top k freq elements instead of storing all n elements 

      # total space complexity = O(n) + O(n) + O(k) - it simplifies to O(n)

