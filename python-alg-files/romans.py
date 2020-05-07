import math

class Romans:
    def intToRoman(self, num: int) -> str:
        numerals = {
            0: '',
            1: 'I',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        romanStr = ''
        tensPlace = 1
        keys = sorted(list(numerals.keys()), reverse=True)
        while num:
            moddedNum = num % 10
            currNum = moddedNum * tensPlace

            if currNum not in numerals:
                remaining = currNum
                startIndex = 0
                tempStr = ''
                while remaining > 0:
                    for ind, item in enumerate(keys[startIndex::]):
                        if remaining - item >= 0:
                            tempStr += numerals.get(item)
                            startIndex += ind
                            remaining -= item
                            break
                romanStr = tempStr + romanStr
            else:
                romanStr = numerals.get(currNum) + romanStr

            num //= 10

            tensPlace = tensPlace * 10

        return romanStr
    
    def digiIterate(self, num: int):
        while num:
            digit = num % 10
            print(digit)
            num //= 10

    # interestingly, same performance as intToRoman, but it's far less complex
    def intToRomanAlt(self, num: int) -> str:
        numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        keys = sorted(list(numerals.keys()), reverse=True)
        romanStr = ''

        for item in keys:
            temp = num // item
            romanStr += numerals.get(item) * temp
            num -= temp * item
        
        return romanStr

runIt = Romans()
print(runIt.intToRomanAlt(60) == 'LX')
print(runIt.intToRomanAlt(80) == 'LXXX')
print(runIt.intToRomanAlt(81) == 'LXXXI')
print(runIt.intToRomanAlt(200) == 'CC')
print(runIt.intToRomanAlt(12) == 'XII')
print(runIt.intToRomanAlt(10) == 'X')
print(runIt.intToRomanAlt(100) == 'C')
print(runIt.intToRomanAlt(3) == 'III')
print(runIt.intToRomanAlt(4) == 'IV')
print(runIt.intToRomanAlt(9) == 'IX')
print(runIt.intToRomanAlt(58) == 'LVIII')
print(runIt.intToRomanAlt(1994) == 'MCMXCIV')