def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    - build from 0 to max(nums)
    - dp[0] = 0
    - dp[1] = 1 * #1's occurence
    - dp[i] = max(dp[i - 1], dp[i - 2] + currGain)
                don't take curr vs. take curr
    
    Main takeaways:
        - take vs. don't take
        - incontinuous data can work if used
        - counter returns 0 if key is not found
    """
    from collections import Counter

    info = Counter(nums)
    for key in info.keys():
        info[key] = info[key] * key
    max_num = max(nums)
    dp = [0] * (max_num + 1)
    dp[0] = 0
    dp[1] = info[1]
    
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], info[i] + dp[i - 2])
    return dp[max_num]

if __name__ == '__main__':
    # arr = [3,4,2]
    arr = [2,2,3,3,3,4]
    print(deleteAndEarn(arr))