def max_consecutive_ones(nums):

    count = 0
    max_count = 0

    for i in range(len(nums)):

        if nums[i] == 1:
            count += 1

        else:
            max_count = max(max_count, count)
            count = 0

    return max(max_count, count)


# User input
nums = list(map(int, input("Enter the array elements: ").split()))

# Function call
result = max_consecutive_ones(nums)

# Output
print("Maximum consecutive 1s:", result)