# leetcode 1822
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
          ans = ans * num

        if ans>0: return +1
        if ans<0: return -1
        if ans==0: return 0