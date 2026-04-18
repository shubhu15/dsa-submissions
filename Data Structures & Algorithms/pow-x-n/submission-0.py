class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(a, b):
            if b==0:
                return 1
            half = pow(a, b//2)
            if b%2==0:
                return half*half
            return half*half*a
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        return pow(x,n)
        