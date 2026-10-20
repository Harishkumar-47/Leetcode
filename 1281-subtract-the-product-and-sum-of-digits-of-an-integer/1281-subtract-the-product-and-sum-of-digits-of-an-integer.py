class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sd = 0
        pd = 1

        while n > 0:
            digit = n % 10
            sd += digit
            pd *= digit
            n //= 10

        return pd - sd