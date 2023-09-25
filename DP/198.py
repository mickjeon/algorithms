'''
House Robber: 
- maximize return
- cannot rob 2 consecutive houses
https://leetcode.com/problems/house-robber/
'''
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        elif i == 1:
            dp[i] = max(nums[0], nums[1])
        else: 
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[len(nums) - 1]

if __name__ == '__main__':
    arr = [1, 3, 5, 6, 2, 3]
    print(rob(arr))