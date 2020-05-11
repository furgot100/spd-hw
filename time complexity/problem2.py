'''Given an array, rotate the array to the right by k steps, where k is non-negative.'''
nums = [1,2,3,4,5,6,7]
k = 3
class Solution:
    def rotate(self, nums):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a


'''Time Complexity'''
'''O(n). use of two lists, one the put the new numbers in and another to copy back to original '''