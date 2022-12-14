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
    counters ={}
    for num in nums:
        if num not in counters:
            counters[num] =0
        counter[num] =+1
    counters

    # find the highest value (the most frequent number)

    max_value = max(counters.values())

    # now we need to see at which index the highest value is at

    for (num, freq) in counters.items():
        if freq == max_value:
            return num
