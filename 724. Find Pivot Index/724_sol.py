def pivotIndex(nums: List[int]) -> int:
        left_sum = 0
        array_sum = sum(nums)
        for i, num in enumerate(nums):
            if left_sum == (array_sum - left_sum - num):
                return i
            else:
                left_sum += num
        return -1