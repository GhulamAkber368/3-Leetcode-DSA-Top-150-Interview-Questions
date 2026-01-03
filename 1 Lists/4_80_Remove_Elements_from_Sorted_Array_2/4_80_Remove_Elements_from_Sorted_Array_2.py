from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0
        c = 0

        for j in range(len(nums)):
            if nums[j] == nums[i]:
                if c < 2:
                    nums[k] = nums[j]
                    k += 1
                    c += 1

            else:
                nums[k] = nums[j]
                k += 1
                i = j
                c = 1

        print("Nums: ", nums[:k])
        print ("K: ", k)

        return k
        
solution = Solution()
solution.removeDuplicates([1,1,1,2,2,3])

        # Time Complexity: O(n)
        # Space Complexity: O(1)