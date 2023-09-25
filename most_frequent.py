from typing import List
from collections import Counter

def find_most_frequent(nums: List[int]) -> int:
    frequencies = {}
    max_frequency = 0
    for num in nums:
        if num not in frequencies:
            frequencies[num] = 0
        frequencies[num] += 1
        max_frequency = max(frequencies[num], max_frequency)
    return max_frequency

def counter_find_most_frequent(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    return Counter(nums).most_common(1).pop(0)[1]


print(find_most_frequent([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
print(counter_find_most_frequent([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
print(find_most_frequent([]))
print(counter_find_most_frequent([]))
print(find_most_frequent([1, 2, 2, 1]))
print(counter_find_most_frequent([1, 2, 2, 1]))