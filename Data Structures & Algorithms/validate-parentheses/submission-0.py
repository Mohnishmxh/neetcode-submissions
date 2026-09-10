class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped bracket matches the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # Valid only if all opened brackets have been matched and cleared
        return not stack
        