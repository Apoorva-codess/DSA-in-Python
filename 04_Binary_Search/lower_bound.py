# ============================================================
# LOWER BOUND
# ============================================================
#
# Lower Bound:
# Find the first index where nums[index] >= target.
#
# Related LeetCode Problem:
# LeetCode 35 - Search Insert Position
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ============================================================


def lower_bound(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:

        # Overflow-safe middle calculation
        mid = low + (high - low) // 2

        # nums[mid] is too small
        if nums[mid] < target:
            low = mid + 1

        # nums[mid] can be the answer
        else:
            high = mid - 1

    return low


# ============================================================
# MAIN PROGRAM
# ============================================================

nums = list(
    map(
        int,
        input("Enter sorted array: ").split()
    )
)

target = int(input("Enter target: "))


result = lower_bound(nums, target)


print("Lower bound index:", result)