def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Original idea:
            3 4 2
            if i delete 3, [] ==> 3
            if i delete 4, [2] ==> 4

            2 3 4 (sorted)
            if i delete 2, [4] f([2,3,4]) = 2 + f(4)
            delete 3, f(2,3,4) = 3 + f([])
            delete 4, f(2,3,4) = 4 + f([2])
            max of these and use memoization.
            BUT, cannot hash lists
        """
        pass

if __name__ == '__main__':
    arr = [3,4,2]
    arr = [2,2,3,3,3,4]
    print(deleteAndEarn(arr))