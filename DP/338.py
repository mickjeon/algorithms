class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        0   0       0
        1   1       1
        2   10      1
        3   11      2  
        4   100     1
        5   101     2
        6   110     2
        7   111     3
        8   1000    1
        """
        # O(nlogn) solution
        # return [bin(i).count('1') for i in range(n + 1)]

        # O(n) solution: leverages the fact that number of bits increase when value is doubled (reverse of bit shifting left by 1)    
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans