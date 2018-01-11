def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    while nums:
        for num in nums:
            print "this is num: ", num
            for other_num in nums:
                if num + other_num == 0:
                    return True
            popped = nums.pop(num)
            print popped

        return False

add_to_zero([0, 1, 2, -2, 1])
