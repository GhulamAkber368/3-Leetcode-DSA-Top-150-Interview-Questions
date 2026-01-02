from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        k = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[k] = nums[j]
                i = j
                k += 1
            j += 1

        print("K: ", k)
        print("Nums: ", nums[:k])

        return k

        # Time Complexity: O(n)
        # Space Complexity: O(1)

solution = Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])