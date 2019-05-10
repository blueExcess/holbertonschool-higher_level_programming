#!/usr/bin/python3
def roman_to_int(rs):
    if rs is None or isinstance(rs, str) == False:
        return 0
    val, total = 0, 0
    nums = []
    legend = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    for i, num in enumerate(rs):
        nums.append(legend.get(num))
        total += nums[i]
        if i > 0:
            if nums[i] > nums[i - 1]:
                total -= (1 + nums[i - 1])
    return total
