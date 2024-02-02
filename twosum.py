class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return []
    
s=Solution()
result=s.twoSum([1,2,7,6],7)
if result:
    for i in result:
        print([i])
else:
    print("Wrong")
