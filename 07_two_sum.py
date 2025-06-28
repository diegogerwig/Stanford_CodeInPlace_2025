def main():
    """
    Calls two_sum_finder on a few sample inputs.
    You can add more test cases here to check your work!
    """
    print(two_sum([2, 7, 11, 15], 9))     # Expected: True
    print(two_sum([1, 2, 3, 4], 8))       # Expected: False
    print(two_sum([5, 5], 10))            # Expected: True
    print(two_sum([4], 8))                # Expected: False

def two_sum(nums, target):
    """
    Returns True if any two distinct elements in the list `nums`
    add up to the value `target`. Otherwise, returns False.
    """
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    main()
