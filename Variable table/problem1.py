# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length
'''Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.'''
nums = [1,1,2]
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x +=1
        return x


# given # =[1,1,2] should return 2 
# start from the first 1 since it doesn't equal the value before it the counter is add 1 so x=1
# then go to the next 1, since it it the same the counter is the same so: x=1
# then go to the 2, 2 != 1 so the counter is added: x=2