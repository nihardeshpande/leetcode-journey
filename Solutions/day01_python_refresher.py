"""
Day 1: Python Refresher
Topics: variables, conditionals, loops, functions, modulo operator, lists

No LeetCode problems yet -- these are warm-up exercises to lock in the basics
before starting the actual pattern-based problem solving.
"""


def is_even(num1):
    """Return True if num1 is even, False if odd."""
    return num1 % 2 == 0


def count_evens(nums):
    """Return how many numbers in the list are even."""
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


def find_max(nums):
    """Return the largest number in the list, without using built-in max()."""
    current_max = nums[0]
    for i in range(len(nums)):
        if current_max < nums[i]:
            current_max = nums[i]
    return current_max


# --- Quick manual tests ---
if __name__ == "__main__":
    print(is_even(4))                          # True
    print(is_even(7))                          # False
    print(count_evens([1, 2, 3, 4, 5, 6]))      # 3
    print(find_max([3, 7, 2, 9, 4]))            # 9
