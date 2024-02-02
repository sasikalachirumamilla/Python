class Solution:
    def reverse(self, x: int) -> int:
        reversed_string=str(x)[::-1]
        if x<0:
            reversed_string='-'+reversed_string[:-1]
        reversed_int=int(reversed_string)
        return reversed_int

s=Solution()
k=s.reverse(-123)
print(k)