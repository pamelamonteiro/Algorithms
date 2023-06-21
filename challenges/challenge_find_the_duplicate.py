def find_duplicate(nums):
    if isinstance(nums, int) is False or nums == "" or nums < 0:
        return False
    sorted(nums)
    for n in range(1, len(nums)):
        if nums[n] == nums[n - 1]:
            return nums[n]
    return False

# https://opensource.com/article/23/1/fix-indexerror-python#:~:text=The%20only%20solution%20to%20fix,()%20an%20len()%20functions.
# https://www.w3schools.com/python/ref_func_isinstance.asp
