class Solution:
    def isValid(self, s: str) -> bool:
        # MENTAL MODEL: 
        # store open brackets in a stack to match them to close brackets later.
        # if we reach closing brackets in the string 
        # check top of the stack 
        # if the bracket at the top of the stack matches the closing bracket 
        # pop off the opening bracket in stack 
        # check matching pairs with most recent/last opening bracket in stack 
        # if the length of the stack is 0 at the end, the string is valid. 

        stack = [] # to temporarily store and remember opening brackets 
        for char in s: # loop through every character in the string 
            if (char == "(" or char == "{" or char == "["): # if the character is an open bracket
                stack.append(char) # add it to the stack to be matched later. 
            else: # otherwise the char is a closing bracket 
                if not stack: # if stack is empty - no open bracket in stack that matches, string is invalid 
                    return False # return false immediately 
                top = stack[-1] # checks most recent bracket in stack 

                # if stack is not empty, to match pairs most recent opening bracket has to match closing bracket. 

                if (char == ")" and top != "("): # mot recent bracket in top has to match opening bracket 
                    return False 
                if(char == "]" and top != "["): 
                    return False 
                if (char == "}" and top != "{"): 
                    return False 

                stack.pop() # by this point matching pair exists, so pop bracket from stack 

        return len(stack) == 0 # if the length of stack is 0, the string is valid 


        # time complexity: O(n)
        # n = max number/length of characters in a string 
        # # all stack functions, stack.append(), if not stack, stack.pop() are O(1)
        # total time complexity = O(n) * O(1) = O(n)

        # space complexity: O(n)
        # worst case: all characters in the string are opening brackets 
        # stack has to store up all n opening brackets that never get popped from stack 
        # stack gets bigger as the input size gets bigger 