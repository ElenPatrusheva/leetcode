class Solution:

    @staticmethod
    def reverse(x: int) -> int:
        def zero(y: int):
            if (y < -2**31) or (y > 2**31 - 1):
                return 0
            else:
                return y
        if x >= 0:
            return zero(int(str(x)[::-1]))
        else:
            return zero(-int(str(x)[:0:-1]))


assert Solution.reverse(12) == 21
assert Solution.reverse(-34) == -43
