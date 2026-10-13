
def search_rotated(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is found
        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[low] <= nums[mid]:

            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Otherwise, right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# User input
nums = list(map(int, input("Enter rotated sorted array: ").split()))
target = int(input("Enter target: "))

result = search_rotated(nums, target)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found")
