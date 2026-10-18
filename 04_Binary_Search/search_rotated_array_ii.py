def search_rotated_ii(nums,target):
    l=0
    h=len(nums)-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]==target:
            return True
        if nums[l]==nums[mid]==nums[h]:
            l=+1
            h=-1
        elif nums[l]<=nums[mid]:
            if nums[l]<=target<nums[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if nums[mid]<target<=nums[h]:
                l=mid+1
            else:
                h=mid-1
    return False
nums=list(map(int,input("Enter the numbers : ").split()))
target=int(input("Enter the target :"))
result = search_rotated_ii(nums, target)
print("Found the target ",result)