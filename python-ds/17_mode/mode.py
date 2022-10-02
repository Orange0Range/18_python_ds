def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count = 0
    highNum = 0

    for num in nums:
        temp = nums.count(num)
        
        if temp > count:
            count = temp
            highNum = num
    
    return highNum