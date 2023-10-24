class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: # 4. 加上負數條件!只要是負的直接錯，0也是錯的
            return False

        while n>1: # 3. 一直下去 比1大就一直做下去
            if n%2 !=0: # 1. 如果n取2有餘數就失敗了
                return False
            n=n//2 # 2. 新的n會是原本n除2  16//2 得到8
        return True