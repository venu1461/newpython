class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for ops in range(1, 61):
            target = num1 - ops * num2
            if target < ops:
                continue
            if bin(target).count('1') <= ops:
                return ops
        return -1
x=Solution()
print(x.makeTheIntegerZero(3,-2)) #output =3