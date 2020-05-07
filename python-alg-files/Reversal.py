class Reversal:
    #given an integer, reverse it. overflows on reversal return 0 (-2^31, 2^31 - 1)
    def reverse(self, x: int) -> int:
        if self.is_overflow(x):
            return 0

        is_negative = True if x < 0 else False
        reversed = 0
        x = abs(x)
        while x:
            temp = x % 10
            reversed = reversed * 10 + temp
            
            x //= 10

        if self.is_overflow(reversed):
            return 0
        
        return -reversed if is_negative else reversed


    def is_overflow(self, x: int) -> bool:
        return x < -2**31 or x > 2**31 - 1
            
runIt = Reversal()
print(runIt.reverse(0) == 0)
print(runIt.reverse(3000000000) == 0)
print(runIt.reverse(123) == 321)
print(runIt.reverse(-123) == -321)
print(runIt.reverse(-111) == -111)
print(runIt.reverse(12) == 21)
print(runIt.reverse(120) == 21)
print(runIt.reverse(1200000) == 21)