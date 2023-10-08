def getMaximumGenerated(n):
    """
    https://leetcode.com/problems/get-maximum-in-generated-array/
    :type n: int
    :rtype: int
    """
    
    dp = [0] * (n + 1)
    max_num = 0
    for i in range(n + 1):
        if i == 0:
            continue
        elif i == 1:
            dp[i] = 1
        elif i % 2 == 0:
            dp[i] = dp[i // 2]
        else:
            j = i // 2
            dp[i] = dp[j] + dp[j + 1]
        max_num = max(max_num, dp[i])
    return max_num

if __name__ == '__main__':
    n = 7
    print(getMaximumGenerated(n))