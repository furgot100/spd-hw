# find the mode in an array that appears more than n/2
nums =[2,3,3,2,2,2]


def mode():
    mode_counter = len(nums)//2
    for num in nums:
        count = sum(1 for elem in nums if elem==num)
        if count > mode_counter:
            return num

mode()

# In order for it to return the count must be greater than 3
# Then it is a nested loop; num stays the same until it can return
# In this case num = 2 while elem is going through the list.
# starting from the first element count = 1
# then count = 2, then count = 3, then count = 4 
# then returns 2 since the count is greater than 3
