'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
-([
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) % 2 != 0:
            return False
        
        openers = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        stack = []

        for elem in s:
            if elem in openers:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                
                prevOpener = stack.pop()
                if elem != openers[prevOpener]:
                    return False
        return len(stack) == 0



runIt = Solution()
print(runIt.isValid('()') == True)
print(runIt.isValid('){') == False)
print(runIt.isValid('(([]))({})') == True)
print(runIt.isValid('()[]{}') == True)
print(runIt.isValid('(]') == False)
print(runIt.isValid('([)]') == False)
print(runIt.isValid('{[]}') == True)
print(runIt.isValid('{([])}') == True)
print(runIt.isValid('{{') == False)
print(runIt.isValid('({}') == False)
print(runIt.isValid('(') == False)
print(runIt.isValid('([][][]){}') == True)

