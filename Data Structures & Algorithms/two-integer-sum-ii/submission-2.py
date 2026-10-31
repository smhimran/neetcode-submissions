class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, i in enumerate(numbers):
            remaining = target - i

            left = 0
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if mid != index and numbers[mid] == remaining:
                    return sorted([index + 1, mid + 1])
                elif numbers[mid] < remaining:
                    left = mid + 1
                else:
                    right = mid - 1

        return [0,0]

