def climbing_stairs(n):
    def dp(i):
        if i <= 2:
            return i
        if i not in memo:
            memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]
    
    '''
    This method utilizes memoization by creating a function that stores a new memo value if i is not seen before.
    The function dp() returns integer to continue count.
    This is a top-down methodology as oppposed to bottom-up
    '''
    memo = {}
    print(dp(n))

if __name__ == '__main__':
    climbing_stairs(3)