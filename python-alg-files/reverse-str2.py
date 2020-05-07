'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        final_str = ''
        counter = 0
        running = True
        while running:
            end = 0
            if counter + (2 * k) < len(s):
                end = counter + (2 * k)
            else:
                end = len(s)
                running = False
            current_chunk = s[counter:end]
            temp = ''
            for index, letter in enumerate(current_chunk):
                if index < k:
                    temp = letter + temp
                else:
                    temp += letter

            final_str += temp
            counter += (2 * k)
        
        return final_str
            

run_it = Solution()
print(run_it.reverseStr('ab', 2) == 'ba')
print(run_it.reverseStr('ab', 1) == 'ab')
print(run_it.reverseStr('abcdefg', 2) == 'bacdfeg')