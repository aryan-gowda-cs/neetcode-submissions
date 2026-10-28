
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        limit = 2147483648 if sign < 0 else INT_MAX

        while x:
            digit = x % 10
            x //= 10

            if res > limit // 10:
                return 0

            if res == limit // 10 and digit > limit % 10:
                return 0

            res = res * 10 + digit

        return sign * res
