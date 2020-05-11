nums =[2,3,3,2,2,2]


def mode():
    mode_counter = len(nums)//2
    for num in nums:
        count = sum(1 for elem in nums if elem==num)
        if count > mode_counter:
            return num

mode()

# Time Complexity
# O(n^2) since there are two nested loops and a brute force way of solveing the problem