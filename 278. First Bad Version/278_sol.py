# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        while n > 0:
            mid = (start + n) // 2
            if not isBadVersion(mid):
                if isBadVersion(mid+1):
                    return mid + 1
                else:
                    start = mid + 1
            else:
                if isBadVersion(mid-1):
                    n = mid - 1
                else:
                    return mid