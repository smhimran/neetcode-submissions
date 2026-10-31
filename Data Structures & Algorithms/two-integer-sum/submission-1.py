class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = defaultdict(int)
        
        for index, num in enumerate(nums): 
            visited[num] = index

        for index, num in enumerate(nums):
            remaining = target - num

            rem_index = visited.get(remaining)

            if rem_index and rem_index != index:
                return [index, rem_index]

        return []