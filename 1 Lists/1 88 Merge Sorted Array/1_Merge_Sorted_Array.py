from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
          
        r = m + n - 1 # 0 are on right side therefore it's easy to compare and place values on right side

        # r = 5, m = 3, n = 2
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[r] = nums1[m-1]
                m -= 1

            else:
                nums1[r] = nums2[n-1]
                n -= 1

            r -= 1

        print("Nums 1: ", nums1)
     
solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)


        # we need to merge num 2 in num 1 therefore using n because it's num 2 length
        # If we replace n with m, after complete traversal of n, n becomes 1. 
        # when n is 1 then if n > 0 condition will broke and else conditio will execute.
        # In else condition n-1 => 1-1 => 0
        # then on next iteration n-1 => 0-1 => -1. It will cause out of index error.
        # Morever then m will start iterating which will keep on decreasing which will cause
        # r negative which will cause again out of index error.
        # Time Complexity: O(m + n)
        # Space Complexity: O(1)

        # New Commit