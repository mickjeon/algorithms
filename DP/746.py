'''
746. Min Cost Climbing Stairs
- Find the minimum cost of climbing the stairs, either by 1 or 2 steps
- 
https://leetcode.com/problems/min-cost-climbing-stairs/
'''
def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    n = len(cost)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            dp[i] = cost[i]
        elif i == n - 2:
            dp[i] = cost[i]
        else:
            dp[i] = min(dp[i + 1], dp[i+2]) + cost[i]
    return min(dp[0], dp[1])

if __name__ == '__main__':
    arr = [1,100,1,1,1,100,1,1,100,1]
    print(minCostClimbingStairs(arr))