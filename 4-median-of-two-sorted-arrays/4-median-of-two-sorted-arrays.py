class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        mid=len(nums)//2
        print(mid)
        if len(nums)%2!=0:
            return nums[mid]
        else:
            med=(nums[mid]+nums[mid-1])/2
            print(med)
            return med
        return 1.0