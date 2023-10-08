def divisorGame(n):
    """
    :type n: int
    :rtype: bool
    n = 2
    - Alice chooses 1 - only choice
    - Bob has no moves
    - Alice wins

    n = 3
    - Alice chooses 1
    2, Bob chooses 1
    
    n = 4
    - Alice choose 2
    2 Bob chooses 1, Alice has no moves
    - Alice chooses 1 > 3, Bob chooses 1 > 2, Alice chooses 1 > Alice wins
    """
    # Mathematical Approach
    # Alice will always win if she can give an odd number to Bob
    return True if n % 2 == 0 else False

    # DP Approach
    # dp = [False] * (n + 1)
    # if n < 2: 
    #     return dp[n]
    # dp[2] = True
    # if n < 4:
    #     return dp[n]
    # for i in range(4, n + 1): 
    #     for j in range(1, i - 1):
    #         if i % j == 0 and dp[j] is True:
    #             dp[i] = True
    #             print(dp)
    #             break
    # return dp[n - 2]

if __name__ == '__main__':
    n = 7
    print(divisorGame(n))