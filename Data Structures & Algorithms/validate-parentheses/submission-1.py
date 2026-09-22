class Solution:
    def isValid(self, s: str) -> bool:
        # MENTAL MODEL: 
        # use stack to store opening brackets 
        # if char is a closing bracket 
        # first check to see if the stack is empty 
        # if not compare the last bracket in the stack to char 
        # if they are matching pop bracket from stack 
        # keep doing this until entire string has been processed 
        # the stack should be empty in the end

        stack = [] # use a stack to store all opening brackets 

        for char in s: # for every character in the string 
            if (char == "(" or char == "{" or char == "["): # if char is any of these open brackets
                stack.append(char) # store it to reference later for match pairs 
            else: # else means char is a closing bracket 
                if not stack: # if stack is empty meaning no open bracket was stored 
                    return False # return False 
                
                top = stack[-1] # this helps us see the stack from the top, or the last element 

                # if no matching pairs exist for curly brackets or last element in stack is not "{"
                # do the same check for ")" and "]"
                if (char == "}" and top != "{"): 
                    return False 
                if (char == "]" and top != "["): 
                    return False 
                if (char == ")" and top != "("):
                    return False 

                # but if a matching pair is found: 

                stack.pop() # pop the opening bracket from the end of stack 
        
        return len(stack) == 0 # if the length of stack is 0, that means there was an opening and closing bracket for every type of bracket, so the input string was valid 

        # Time Complexity: 
        # - loop through n characters in string s - O(n)
        # - if statements, appending, and popping in stack are O(1)
        # - total time complexity = O(n) * O(1) = O(n)

        # Space Complexity:
        # - Think about data structures being used or created 
        # - worst case every character in input is an opening bracket so the stack stores all od them, ex: stack = "(((("
        # - stack has to store up to n characters that will never get popped because no matchig closing brackets exist. 
        # - total space complexity - O(n)