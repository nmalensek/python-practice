'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
row 1: 0   4   8    12
row 2: 1 3 5 7 9  11  13
row 3: 2   6   10

4 rows:
P     I    N
A   L S  I G
Y A   H R
P     I
'PINALSIGYAHRPI'
row 1: 0    6       12 
row 2: 1  5 7    11 13
row 3: 2 4  8 10
row 4: 3    9

5 rows:
P     H
A   S I
Y  I  R
P L   I G
A     N
'PHASIYIRPLIGAN'
3       4      5
4th vs 6th vs 8th
= (r * 2) - 2
row 0: 0,      8
row 1: 1,    7, 9
row 2: 2,   6, 10
row 3: 3, 5,   11, 13
row 4: 4,      12
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 0:
            return s
        rows = []
        for _ in range(numRows):
            rows.append([])
        # count up until numRows - 1, then back down then back up till end of string.
        current_row = 0
        in_reverse = False
        for letter in s:
            rows[current_row].append(letter)

            if not in_reverse:
                current_row += 1
            else:
                current_row -= 1

            if current_row == numRows - 1 or current_row == 0:
                in_reverse = not in_reverse
        
        zig_zag = ''

        for row in rows:
            for letter in row:
                zig_zag += letter
        
        return zig_zag
        




run_it = Solution()
print(run_it.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(run_it.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(run_it.convert('AB', 1) == 'AB')