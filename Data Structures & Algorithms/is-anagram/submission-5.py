class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
   

        # Use frequency maps where each character is the key
        # and its frequency/count is the value.

        # Build one frequency map for s and one for t.
        # If both maps contain the same characters with the same
        # frequencies, then s and t are anagrams.

        seenS = {}  # Empty frequency map for s
        seenT = {}  # Empty frequency map for t

        # Strings are iterable in Python, so we can loop through
        # their characters directly.
        for char in s:

            # "char in seenS" checks whether char exists as a KEY
            # in the dictionary. Key lookup is O(1) average time.
            if char in seenS:
                seenS[char] += 1  # Increment existing frequency
            else:
                seenS[char] = 1   # First occurrence: initialize count to 1

        for char in t:
            if char in seenT:
                seenT[char] += 1
            else:
                seenT[char] = 1

        # Dictionary equality checks whether both dictionaries contain
        # the same key-value pairs. Dictionary order does not matter.
        if seenS == seenT:
            return True

        return False


# Time Complexity = O(n + m)
# n is the length of string s and m is the length of string t.
# We loop through s once, which takes O(n), and then loop through t once,
# which takes O(m). Since the loops happen one after another, we add them:
# O(n) + O(m) = O(n + m).
# If s and t must have the same length, this can also be simplified to O(n).


# Space Complexity = O(n + m) or O(1)
# We create two hashmaps: one stores the character frequencies from s,
# and the other stores the character frequencies from t.
# In the worst case, the first hashmap can store up to n unique characters
# and the second can store up to m unique characters, so the total extra
# space is O(n + m).
# If the problem only allows a fixed set of characters, such as 26 lowercase
# English letters, the space can technically be considered O(1). - consider O(1)