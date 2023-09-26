'''
House Robber 2: 
- maximize return
- cannot rob 2 consecutive houses
- However, it is a circular array; index 0 and index n - 1 are next to each other
https://leetcode.com/problems/house-robber-ii/
'''
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    # rob 1st house --> nums[:length - 1]
    # did not rob 1st house --> nums[1:]
    n = len(nums) - 1
    x = nums[:n]
    y = nums[1:]
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if i == 0:
            a[i] = x[0]
            b[i] = y[0]
        elif i == 1:
            a[i] = max(x[0], x[1])
            b[i] = max(y[0], y[1])
        else:
            a[i] = max(a[i - 1], a[i - 2] + x[i])
            b[i] = max(b[i - 1], b[i - 2] + y[i])
    return max(a[n - 1], b[n - 1])

if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    print(rob(arr))