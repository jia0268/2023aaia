class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: # 4. 加上負數條件!只要是負的直接錯，0也是錯的
            return False

        while n>1: # 3. 一直下去 比1大就一直做下去
            if n%4 !=0: # 1. 如果n取4有餘數就失敗了
                return False
            n=n//4 # 2. 新的n會是原本n除4  16//4 得到4
        return True
