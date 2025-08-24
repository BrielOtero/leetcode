class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        time: O(n)
        space: O(1)
        approach: Two pointers
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return []
