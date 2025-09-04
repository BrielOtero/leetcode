class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        time: O(n^2)
        space: O(n)
        approach: two pointers
        """
        triplets = []
        nums.sort()  # Timsort O(n)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return triplets
