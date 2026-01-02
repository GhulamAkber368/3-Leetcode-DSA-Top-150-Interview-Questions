from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1

        print("Nums: ", nums)
        print("I: ", i)

        return i

        # Time Comlexity: O(n)
        # Space Complexity: O(1)

solution = Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])