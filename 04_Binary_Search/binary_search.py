def binary_search_iterative(nums, target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid= low+(high-low)//2 #for overflow case as well
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
def binary_search_recursive(nums,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binary_search_recursive(nums,mid+1,high,target)
    else:
        return binary_search_recursive(nums,low,mid-1,target)
#main program
nums=list(map(int,input("Enter the nos:").split()))
target=int(input("Enter the number : "))
iterative_result=binary_search_iterative(nums,target)
recursive_result=binary_search_recursive(nums,0,len(nums)-1,target)
# iterative result
if iterative_result != -1:
    print("Target found at index:", iterative_result)
else:
    print("Target not found")
#recursive result
if recursive_result != -1:
    print("Target found at index:", recursive_result)
else:
    print("Target not found")