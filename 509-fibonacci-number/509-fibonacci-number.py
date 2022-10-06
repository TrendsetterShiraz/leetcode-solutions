class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        
        for _ in repeat(None, n):
            a, b = b, a+b
        return a