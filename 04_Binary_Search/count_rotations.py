def find_rotations(nums):
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid
    return low
nums=list(map(int,input("Enter the nos. ").split()))
result=find_rotations(nums)
print("The no. of rotations are : ",result)
